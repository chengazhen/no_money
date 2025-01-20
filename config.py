from dotenv import load_dotenv
import os
import sys
from logger import logging


class Config:
    def __init__(self):
        # 获取应用程序的根目录路径
        if getattr(sys, "frozen", False):
            # 如果是打包后的可执行文件
            application_path = os.path.dirname(sys.executable)
        else:
            # 如果是开发环境
            application_path = os.path.dirname(os.path.abspath(__file__))

        # 指定 .env 文件的路径
        dotenv_path = os.path.join(application_path, ".env")

        if not os.path.exists(dotenv_path):
            raise FileNotFoundError(f"文件 {dotenv_path} 不存在")

        # 加载 .env 文件
        load_dotenv(dotenv_path)

        self.imap = False
        self.temp_mail = os.getenv("TEMP_MAIL", "").strip().split("@")[0]
        self.domain = os.getenv("DOMAIN", "").strip()

        # 如果临时邮箱为null则加载IMAP
        if self.temp_mail == 'null':
            self.imap = True
            self.imap_server = os.getenv("IMAP_SERVER", "").strip()
            self.imap_port = os.getenv("IMAP_PORT", "").strip()
            self.imap_user = os.getenv("IMAP_USER", "").strip()
            self.imap_pass = os.getenv("IMAP_PASS", "").strip()
            self.imap_dir = os.getenv("IMAP_DIR", "inbox").strip()

        self.check_config()

    def get_temp_mail(self):

        return self.temp_mail

    def get_imap(self):
        if not self.imap:
            return False
        return {
            "imap_server": self.imap_server,
            "imap_port": self.imap_port,
            "imap_user": self.imap_user,
            "imap_pass": self.imap_pass,
            "imap_dir": self.imap_dir
        }

    def get_domain(self):
        return self.domain

    def check_config(self):
        if not self.check_is_valid(self.temp_mail):
            raise ValueError("临时邮箱未配置，请在 .env 文件中设置 TEMP_MAIL")
        if not self.check_is_valid(self.domain):
            raise ValueError("域名未配置，请在 .env 文件中设置 DOMAIN")
        if not self.imap_server == 'null' and not self.check_is_valid(self.imap_server):
            raise ValueError("IMAP服务器未配置，请在 .env 文件中设置 IMAP_SERVER")
        if not self.imap_port == 'null' and not self.check_is_valid(self.imap_port):
            raise ValueError("IMAP端口未配置，请在 .env 文件中设置 IMAP_PORT")
        if not self.imap_user == 'null' and not self.check_is_valid(self.imap_user):
            raise ValueError("IMAP用户名未配置，请在 .env 文件中设置 IMAP_USER")
        if not self.imap_pass == 'null' and not self.check_is_valid(self.imap_pass):
            raise ValueError("IMAP密码未配置，请在 .env 文件中设置 IMAP_PASS")
        if not self.imap_dir == 'null' and not self.check_is_valid(self.imap_dir):
            raise ValueError("IMAP收件箱目录未配置，请在 .env 文件中设置 IMAP_DIRECTORY")

    def check_is_valid(self, str):
        return len(str.strip()) > 0

    def print_config(self):
        # logging.info(f"\033[32m临时邮箱: {self.temp_mail}\033[0m")
        if self.imap:
            logging.info(f"\033[32mIMAP服务器: {self.imap_server}\033[0m")
            logging.info(f"\033[32mIMAP端口: {self.imap_port}\033[0m")
            logging.info(f"\033[32mIMAP用户名: {self.imap_user}\033[0m")
            logging.info(f"\033[32mIMAP密码: {'*' * len(self.imap_pass)}\033[0m")
            logging.info(f"\033[32mIMAP收件箱目录: {self.imap_dir}\033[0m")
        if self.temp_mail != 'null':
            logging.info(f"\033[32m临时邮箱: {self.temp_mail}@{self.domain}\033[0m")
        logging.info(f"\033[32m域名: {self.domain}\033[0m")


# 使用示例
if __name__ == "__main__":
    try:
        config = Config()
        print("环境变量加载成功！")
        config.get_temp_mail()
        config.get_domain()
    except ValueError as e:
        print(f"错误: {e}")
