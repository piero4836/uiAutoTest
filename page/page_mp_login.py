from time import sleep

import page
from base.web_base import WebBase


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_user_name(self,username):
        self.base_input(page.mp_username,username)

    # 输入验证码
    def page_input_password(self,password):
        self.base_input(page.mp_password,password)

    # 点击登录按钮
    def page_click_login(self):
        self.base_click(page.mp_login_btn)
        sleep(5)


    # 获取昵称封装 ->> 测试脚本中断言调用
    def page_get_nickname(self):
        sleep(2)
        return self.base_get_text(page.mp_nickname)

    def page_app_add_click(self):
        sleep(2)
        self.base_click(page.mp_app_add_btn)

    # 组合业务功能 ->> 测试脚本中调用
    def page_mp_login(self,username,password):
        self.page_input_user_name(username)
        self.page_input_password(password)
        self.page_click_login()

    # 组合业务功能 ->> app测试脚本中调用
    def page_mp_login_success(self,username="admin",password="123456"):
        self.page_input_user_name(username)
        self.page_input_password(password)
        self.page_click_login()

