import random

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestApp:

    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_mp)
        self.page_in = PageIn(driver)
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        self.app = self.page_in.page_get_PageMpApp()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("versionName,expect",read_yaml("mp_app.yaml"))
    def test_mp_app(self,versionName,expect):
        version = "".join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
        self.app.page_mp_app(versionName, version)
        assert self.app.page_app_info() in version


