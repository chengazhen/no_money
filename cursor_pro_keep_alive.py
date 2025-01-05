import os
from colorama import Fore, Style, init

# 初始化colorama
init()

# 定义emoji和颜色常量
EMOJI = {
    'START': '🚀',
    'FORM': '📝',
    'VERIFY': '🔄',
    'PASSWORD': '🔑',
    'CODE': '📱',
    'DONE': '✨',
    'ERROR': '❌',
    'WAIT': '⏳',
    'SUCCESS': '✅',
    'MAIL': '📧'
}

os.environ["PYTHONVERBOSE"] = "0"
os.environ["PYINSTALLER_VERBOSE"] = "0"

import time
import random
from cursor_auth_manager import CursorAuthManager
import os
import logging
from browser_utils import BrowserManager
from get_email_code import EmailVerificationHandler
from logo import print_logo

# 在文件开头设置日志
class ColoredFormatter(logging.Formatter):
    """自定义彩色日志格式器"""
    
    def format(self, record):
        if record.levelno == logging.INFO:
            record.msg = f"{Fore.CYAN}{record.msg}{Style.RESET_ALL}"
        elif record.levelno == logging.ERROR:
            record.msg = f"{Fore.RED}{EMOJI['ERROR']} {record.msg}{Style.RESET_ALL}"
        return super().format(record)

# 修改日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("cursor_keep_alive.log", encoding="utf-8"),
    ],
)

# 为控制台处理器设置彩色格式器
for handler in logging.getLogger().handlers:
    if isinstance(handler, logging.StreamHandler):
        handler.setFormatter(ColoredFormatter("%(asctime)s - %(levelname)s - %(message)s"))


def show_progress(progress, total, prefix='Progress:', suffix='Complete', length=50):
    filled_length = int(length * progress / total)
    bar = Fore.GREEN + '█' * filled_length + Fore.WHITE + '░' * (length - filled_length)
    percent = f"{100.0 * progress / total:.1f}"
    print(f'\r{Fore.CYAN}{prefix} |{bar}| {Fore.YELLOW}{percent}%{Fore.BLUE} {suffix}{Style.RESET_ALL}', end='', flush=True)
    if progress == total:
        print()


def handle_turnstile(tab):
    print(f"{Fore.CYAN}{EMOJI['VERIFY']} 开始突破 Turnstile 验证{Style.RESET_ALL}")
    try:
        while True:
            try:
                challengeCheck = (
                    tab.ele("@id=cf-turnstile", timeout=2)
                    .child()
                    .shadow_root.ele("tag:iframe")
                    .ele("tag:body")
                    .sr("tag:input")
                )

                if challengeCheck:
                    print(f"{Fore.YELLOW}{EMOJI['WAIT']} 检测到验证请求，开始处理...{Style.RESET_ALL}")
                    time.sleep(random.uniform(1, 3))
                    challengeCheck.click()
                    time.sleep(2)
                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证突破成功！{Style.RESET_ALL}")
                    return True
            except:
                pass

            if tab.ele("@name=password"):
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证通过{Style.RESET_ALL}")
                break
            if tab.ele("@data-index=0"):
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证通过{Style.RESET_ALL}")
                break
            if tab.ele("Account Settings"):
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 验证通过{Style.RESET_ALL}")
                break

            time.sleep(random.uniform(1, 2))
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} 验证失败: {str(e)}{Style.RESET_ALL}")
        return False


def get_cursor_session_token(tab, max_attempts=3, retry_interval=2):
    """
    获取Cursor会话token，带有重试机制
    :param tab: 浏览器标签页
    :param max_attempts: 最大尝试次数
    :param retry_interval: 重试间隔(秒)
    :return: session token 或 None
    """
    print(f"{Fore.CYAN}{EMOJI['WAIT']} 开始获取 Cursor Session Token...{Style.RESET_ALL}")
    attempts = 0

    while attempts < max_attempts:
        try:
            cookies = tab.cookies()
            for cookie in cookies:
                if cookie.get("name") == "WorkosCursorSessionToken":
                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Token 获取成功{Style.RESET_ALL}")
                    return cookie["value"].split("%3A%3A")[1]

            attempts += 1
            if attempts < max_attempts:
                print(
                    f"{Fore.YELLOW}{EMOJI['WAIT']} 第 {attempts} 次尝试未获取到 Token，{retry_interval}秒后重试...{Style.RESET_ALL}"
                )
                time.sleep(retry_interval)
            else:
                print(f"{Fore.RED}{EMOJI['ERROR']} 已达到最大尝试次数({max_attempts})，获取 Token 失败{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} 获取 Token 失败: {str(e)}{Style.RESET_ALL}")
            attempts += 1
            if attempts < max_attempts:
                print(f"{Fore.YELLOW}{EMOJI['WAIT']} 将在 {retry_interval} 秒后重试...{Style.RESET_ALL}")
                time.sleep(retry_interval)

    return None


def update_cursor_auth(email=None, access_token=None, refresh_token=None):
    """
    更新Cursor的认证信息的便捷函数
    """
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{EMOJI['WAIT']} 正在更新 Cursor 认证信息...{Style.RESET_ALL}")
    
    auth_manager = CursorAuthManager()
    result = auth_manager.update_auth(email, access_token, refresh_token)
    
    if result:
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 邮箱信息更新成功{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Access Token 更新成功{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Refresh Token 更新成功{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{EMOJI['DONE']} 认证信息更新完成{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{EMOJI['ERROR']} 认证信息更新失败{Style.RESET_ALL}")
    
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    return result


def sign_up_account(browser, tab):
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['START']} 开始 Cursor Pro 注册流程{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[信息]{Style.RESET_ALL}")
    print(f"{EMOJI['FORM']} 邮箱服务商: {Fore.GREEN}mailto.plus{Style.RESET_ALL}")
    print(f"{EMOJI['FORM']} 临时邮箱地址: {Fore.GREEN}{account}{Style.RESET_ALL}")
    print(f"{EMOJI['FORM']} 注册名称: {Fore.GREEN}{first_name} {last_name}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n")
    
    total_steps = 5
    show_progress(0, total_steps)
    tab.get(sign_up_url)

    try:
        if tab.ele("@name=first_name"):
            print(f"\n{Fore.YELLOW}{EMOJI['FORM']} [1/5] 填写注册信息...{Style.RESET_ALL}")
            tab.actions.click("@name=first_name").input(first_name)
            time.sleep(random.uniform(1, 3))

            tab.actions.click("@name=last_name").input(last_name)
            time.sleep(random.uniform(1, 3))

            tab.actions.click("@name=email").input(account)
            time.sleep(random.uniform(1, 3))

            tab.actions.click("@type=submit")
            show_progress(1, total_steps)

    except Exception as e:
        print(f"\n{Fore.RED}{EMOJI['ERROR']} 打开注册页面失败{Style.RESET_ALL}")
        return False

    print(f"\n{Fore.YELLOW}{EMOJI['VERIFY']} [2/5] 处理验证...{Style.RESET_ALL}")
    handle_turnstile(tab)
    show_progress(2, total_steps)

    try:
        if tab.ele("@name=password"):
            print(f"\n{Fore.YELLOW}{EMOJI['PASSWORD']} [3/5] 设置密码...{Style.RESET_ALL}")
            tab.ele("@name=password").input(password)
            time.sleep(random.uniform(1, 3))

            tab.ele("@type=submit").click()
            print(f"{Fore.CYAN}{EMOJI['WAIT']} 请稍等...{Style.RESET_ALL}")
            show_progress(3, total_steps)

    except Exception as e:
        print(f"\n{Fore.RED}{EMOJI['ERROR']} 执行失败{Style.RESET_ALL}")
        return False

    time.sleep(random.uniform(1, 3))
    if tab.ele("This email is not available."):
        print(f"\n{Fore.RED}{EMOJI['ERROR']} 执行失败{Style.RESET_ALL}")
        return False

    print(f"\n{Fore.YELLOW}{EMOJI['CODE']} [4/5] 处理验证码...{Style.RESET_ALL}")
    handle_turnstile(tab)
    show_progress(4, total_steps)

    while True:
        try:
            if tab.ele("Account Settings"):
                break
            if tab.ele("@data-index=0"):
                code = email_handler.get_verification_code(account)
                if not code:
                    return False

                i = 0
                for digit in code:
                    tab.ele(f"@data-index={i}").input(digit)
                    time.sleep(random.uniform(0.1, 0.3))
                    i += 1
                break
        except Exception as e:
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")

    print(f"\n{Fore.YELLOW}{EMOJI['DONE']} [5/5] 完成注册...{Style.RESET_ALL}")
    handle_turnstile(tab)
    wait_time = random.randint(3, 6)
    for i in range(wait_time):
        print(f"{Fore.CYAN}{EMOJI['WAIT']} 等待中... {wait_time-i}秒{Style.RESET_ALL}")
        time.sleep(1)
    
    # 获取可用额度
    total_usage = "未知"
    tab.get(settings_url)
    try:
        usage_selector = (
            "css:div.col-span-2 > div > div > div > div > "
            "div:nth-child(1) > div.flex.items-center.justify-between.gap-2 > "
            "span.font-mono.text-sm\\/\\[0\\.875rem\\]"
        )
        usage_ele = tab.ele(usage_selector)
        if usage_ele:
            usage_info = usage_ele.text
            total_usage = usage_info.split("/")[-1].strip()
    except Exception as e:
        print(f"\n{Fore.RED}{EMOJI['ERROR']} 获取可用额度失败: {str(e)}{Style.RESET_ALL}")

    # 显示最终信息
    print(f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Cursor Pro 注册成功！{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[账号信息]{Style.RESET_ALL}")
    print(f"{EMOJI['SUCCESS']} 邮箱: {Fore.GREEN}{account}{Style.RESET_ALL}")
    print(f"{EMOJI['SUCCESS']} 密码: {Fore.GREEN}{password}{Style.RESET_ALL}")
    print(f"{EMOJI['SUCCESS']} 可用额度: {Fore.GREEN}{total_usage}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    
    # 记录到日志
    account_info = (
        f"\n{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n"
        f"{Fore.CYAN}Cursor Pro 账号信息{Style.RESET_ALL}\n"
        f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}\n"
        f"{EMOJI['FORM']} 邮箱服务商: {Fore.GREEN}mailto.plus{Style.RESET_ALL}\n"
        f"{EMOJI['MAIL']} 邮箱: {Fore.GREEN}{account}{Style.RESET_ALL}\n"
        f"{EMOJI['PASSWORD']} 密码: {Fore.GREEN}{password}{Style.RESET_ALL}\n"
        f"{EMOJI['SUCCESS']} 可用额度: {Fore.GREEN}{total_usage}{Style.RESET_ALL}\n"
        f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}"
    )
    logging.info(account_info)
    time.sleep(5)
    return True


class EmailGenerator:
    def __init__(
        self,
        domain="mailto.plus",
        password="".join(
            random.choices(
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*",
                k=12,
            )
        ),
        first_name="yuyan",
        last_name="peng",
    ):
        self.domain = domain
        self.default_password = password
        self.default_first_name = first_name
        self.default_last_name = last_name

    def generate_email(self, length=8):
        """生成随机邮箱地址"""
        random_str = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=length))
        timestamp = str(int(time.time()))[-6:]  # 使用时间戳后6位
        return f"{random_str}{timestamp}@{self.domain}"

    def get_account_info(self):
        """获取完整的账号信息"""
        return {
            "email": self.generate_email(),
            "password": self.default_password,
            "first_name": self.default_first_name,
            "last_name": self.default_last_name,
        }


if __name__ == "__main__":
    print_logo()
    browser_manager = None
    try:
        # 初始化浏览器
        browser_manager = BrowserManager()
        browser = browser_manager.init_browser()

        # 初始化邮箱验证处理器
        email_handler = EmailVerificationHandler(browser)

        # 固定的 URL 配置
        login_url = "https://authenticator.cursor.sh"
        sign_up_url = "https://authenticator.cursor.sh/sign-up"
        settings_url = "https://www.cursor.com/settings"
        mail_url = "https://tempmail.plus"

        # 生成随机邮箱
        email_generator = EmailGenerator()
        account = email_generator.generate_email()
        password = email_generator.default_password
        first_name = email_generator.default_first_name
        last_name = email_generator.default_last_name

        auto_update_cursor_auth = True

        tab = browser.latest_tab
        tab.run_js("try { turnstile.reset() } catch(e) { }")

        tab.get(login_url)

        if sign_up_account(browser, tab):
            token = get_cursor_session_token(tab)
            if token:
                update_cursor_auth(
                    email=account, access_token=token, refresh_token=token
                )
            else:
                print(f"{Fore.RED}{EMOJI['ERROR']} 账户注册失败{Style.RESET_ALL}")

        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} 所有操作执行完毕{Style.RESET_ALL}")

    except Exception as e:
        logging.error(f"程序执行出错: {str(e)}")
        import traceback
        logging.error(traceback.format_exc())
    finally:
        if browser_manager:
            browser_manager.quit()
        input(f"\n{Fore.CYAN}{EMOJI['WAIT']} 按回车键退出...{Style.RESET_ALL}")