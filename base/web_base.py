from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from base.base import Base


class WebBase(Base):

    def web_click_element(self,placeholder_text,click_text):

        #点击复选框
        loc = By.CSS_SELECTOR, ".el-select--small"
        self.base_click(loc)
        #暂停
        #sleep(2)
        #选择包含指定文本
        loc = (By.XPATH, "//span[text()='{}']".format(click_text))
        self.base_click(loc)

    def web_element_is_exist(self,text):
        loc = (By.XPATH, "//*[text()={}]".format(text))
        try:
            self.base_find(loc, timeout=3)
            print("找到元素: ",loc)
            return True
        except Exception as e:
            print("没有找到元素: ",loc)
            return False



