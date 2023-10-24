from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# 指定驱动
web = webdriver.Firefox()
# s = Service(r"./chromedriver_mac64/chromedriver")
# web = webdriver.Chrome(service=s)
# 发起请求
web.get('https://login.taobao.com/')
# 登录名标签定位
username_input = web.find_element(By.NAME,'fm-login-id')
# 标签交互
username_input.send_keys('皮卡丘_super秋')

pwd_input = web.find_element(By.NAME,'fm-login-password')

pwd_input.send_keys('yjq@863064604')

# 定位登录标签
btn = web.find_element(By.CSS_SELECTOR,'.fm-btn')
# 点击登录
btn.click()
# 模拟拖拽动作
slider = web.find_element(By.ID, 'nc_1_n1z')
action = ActionChains(web)
action.click_and_hold(slider).perform()
action.move_by_offset(258, 0).perform()  # 根据实际情况调整拖拽距离
time.sleep(300)  # 等待一段时间，以便验证成功
action.release().perform()

# 定位登录标签
btn = web.find_element(By.CSS_SELECTOR,'.fm-btn')
# 点击登录
btn.click()
time.sleep(5000)
web.quit()
