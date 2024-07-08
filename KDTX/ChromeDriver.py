# 导包
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
driver.maximize_window()

# 访问登录页
driver.get("https://www.baidu.com/")
time.sleep(3)

# 关闭浏览器
driver.quit()

