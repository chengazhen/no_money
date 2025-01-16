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

        self.temp_mail = os.getenv("TEMP_MAIL", "").strip().split("@")[0]
        self.domain = os.getenv("DOMAIN", "").strip()

        self.check_config()

    def get_temp_mail(self):

        return self.temp_mail

    def get_domain(self):
        return self.domain

    def check_config(self):
        if not self.check_is_valid(self.temp_mail):
            raise ValueError("临时邮箱未配置，请在 .env 文件中设置 TEMP_MAIL")
        if not self.check_is_valid(self.domain):
            raise ValueError("域名未配置，请在 .env 文件中设置 DOMAIN")

        logging.info(f"\033[32m临时邮箱: {self.temp_mail}\033[0m")
        logging.info(f"\033[32m域名: {self.domain}\033[0m")

    def check_is_valid(self, str):
        return len(str.strip()) > 0


# 使用示例
if __name__ == "__main__":
    try:
        config = Config()
        print("环境变量加载成功！")
        config.get_temp_mail()
        config.get_domain()
    except ValueError as e:
        print(f"错误: {e}")
