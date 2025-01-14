from DrissionPage.common import Keys
import time
import re
from config import Config


class EmailVerificationHandler:
    def __init__(self, browser, mail_url="https://tempmail.plus"):
        self.browser = browser
        self.mail_url = mail_url
        self.username = Config().get_temp_mail()

    def get_verification_code(self):
        code = None

        try:
            print("正在处理...")
            # 打开新标签页访问临时邮箱
            tab_mail = self.browser.new_tab(self.mail_url)
            self.browser.activate_tab(tab_mail)

            # 输入用户名
            self._input_username(tab_mail)

            # 手动输入验证码
            code = input("请输入验证码: ")

            # 清理邮件
            self._cleanup_mail(tab_mail)

            # 关闭标签页
            tab_mail.close()

        except Exception as e:
            print(f"获取验证码失败: {str(e)}")

        return code

    def _input_username(self, tab):
        while True:
            if tab.ele("@id=pre_button"):
                tab.actions.click("@id=pre_button")
                time.sleep(0.5)
                tab.run_js('document.getElementById("pre_button").value = ""')
                time.sleep(0.5)
                tab.actions.input(self.username).key_down(Keys.ENTER).key_up(Keys.ENTER)
                break
            time.sleep(1)

    def _cleanup_mail(self, tab):
        if tab.ele("@id=delete_mail"):
            tab.actions.click("@id=delete_mail")
            time.sleep(1)

        if tab.ele("@id=confirm_mail"):
            tab.actions.click("@id=confirm_mail")
