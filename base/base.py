from time import sleep

import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog().get_logger()
class Base:

    #初始化
    def __init__(self,driver):
        log.info("正在初始化driver: {}".format(driver))
        self.driver = driver

    #查找 方法封装
    def base_find(self,loc, timeout=30, poll=2):
        """
        :param loc: 格式为列表或者元祖
        :param timeout: 查找元素超时时间
        :param poll: 查找元素的频率
        :return: 返回元素
        """
        log.info("正在查找元素: {}".format(loc))
        return WebDriverWait(
            self.driver,
            timeout=timeout,
            poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #输入 方法封装
    def base_input(self,loc,value):
        #1 获取元素
        el = self.base_find(loc)
        #2 清空文本
        log.info("正在对 {} 元素执行清空操作".format(loc))
        el.clear()
        #3 输入操作
        log.info("正在对 {} 元素执行输入操作".format(loc))
        el.send_keys(value)

    #点击 方法封装
    def base_click(self,loc):
        #获取元素并点击
        self.base_find(loc).click()
        sleep(1)

    #获取 元素文本
    def base_get_text(self,loc):
        log.info("正在对 {} 元素执行获取文本操作".format(loc))
        return self.base_find(loc).text

    #截图
    def base_get_img(self):
        #调用截图方法
        self.driver.get_screenshot_as_file("../image/error.png")
        #调用图片写入报告文件方法
        self.__base_write_img()

    #将图片写入报告文件
    def __base_write_img(self):
        #获取图片流
        with open("../image/error.png", "rb") as f:
            #调用allure.attach附加方法
            allure.attach("错误原因: ", f.read(), allure.attachment_type.PNG)


