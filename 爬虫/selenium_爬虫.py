# 导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 指定驱动
web = webdriver.Chrome(executable_path='./chromedriver_mac64/chromedriver')
# 发起请求
web.get('https://www.taobao.com/')
#滚动
web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(3)
# 登录名标签定位
username_input = web.find_element(By.NAME,'q')
# 标签交互
username_input.send_keys('茶叶')

# 点击搜索
btn = web.find_element(By.CLASS_NAME,'btn-search')
# 点击搜索
btn.click()
time.sleep(10)
web.quit()