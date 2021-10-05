import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import pytest

from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
class TestMpLogin:
    #初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()
        self.app = PageIn(driver).page_get_PageMpApp()


    #结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    #测试业务方法
    @pytest.mark.parametrize("username,password,expect",read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, password, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username,password)
        self.app.page_mp_app("1", "2")
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            #输出错误信息
            log.error("错误原因:{}".format(e))
            print("错误原因:",e)
            #截图
            self.mp.base_get_img()
            #抛异常
            raise



