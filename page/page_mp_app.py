from time import sleep

import page
from base.web_base import WebBase


class PageMpApp(WebBase):

    def page_list_app(self):
        #sleep(2)
        self.base_click(page.mp_app_list)

    def page_app_add_click(self):
        #sleep(2)
        self.base_click(page.mp_app_add_btn)

    def page_app_input_version_name(self, versionName):
        self.base_input(page.mp_app_version_name, versionName)

    def page_app_input_version(self, version):
        self.base_input(page.mp_app_version, version)

    def page_app_select_type(self):
        #sleep(2)
        self.web_click_element(placeholder_text="请选择", click_text="口罩")

    def page_app_submit(self):
        self.base_click(page.mp_app_submit)

    def page_app_info(self):
        sleep(2)
        version = self.base_get_text(page.mp_app_info)
        print(version)
        return version

    def page_mp_app(self,versionName,version):
        self.page_list_app()
        self.page_app_add_click()
        self.page_app_input_version_name(versionName)
        self.page_app_input_version(version)
        self.page_app_select_type()
        self.page_app_submit()



