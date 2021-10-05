from selenium.webdriver.chrome import webdriver

from selenium import webdriver
class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 2.获取webdriver方法
    @classmethod
    def get_web_driver(cls,url):
        #driver非空判断
        if cls.__web_driver is None:
            #获取浏览器
            cls.__web_driver = webdriver.Chrome()
            #最大化浏览器
            cls.__web_driver.maximize_window()
            #打开url
            cls.__web_driver.get(url)
            return cls.__web_driver
        else:
            return cls.__web_driver

    # 3.退出webdriver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None


