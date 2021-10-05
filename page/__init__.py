"""以下数据为自媒体配置数据"""

from selenium.webdriver.common.by import By

url_mp = "http://localhost:8080/"

url_mis = "http://ttmis.research.itcast.cn/"

#用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入用户名']")
#验证码
mp_password = (By.CSS_SELECTOR, "[placeholder='请输入密码']")
#登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
#昵称
mp_nickname = (By.CSS_SELECTOR, ".nickname")

mp_app_list = (By.XPATH, "//span[text()='APP管理']/..")

mp_app_add_btn = (By.XPATH, "//span[text()='新增']/..")

mp_app_version_name = (By.CSS_SELECTOR, "[placeholder='请输入版本名称']")

mp_app_version = (By.CSS_SELECTOR, "[placeholder='请输入版本号']")

mp_app_type_select = (By.CSS_SELECTOR, "[placeholder='请输入版本号']")

mp_app_submit = (By.XPATH, "//span[text()='保存']/..")

mp_app_info = (By.XPATH, "//tr[@class='el-table__row']/td")





