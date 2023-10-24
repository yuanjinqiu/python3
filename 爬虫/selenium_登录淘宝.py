from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# 设置浏览器参数
options = Options()
options.add_argument('--headless')  # 无头浏览器模式
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36')

# 设置代理IP
chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(chrome_options=chrome_options)

# 登录淘宝
driver.get('https://login.taobao.com')
time.sleep(2)
driver.find_element(By.ID,'fm-login-id').send_keys('皮卡丘_super秋')
driver.find_element(By.ID,'fm-login-password').send_keys('')
time.sleep(1)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(5)


wait = WebDriverWait(driver, 10)
slider = wait.until(EC.element_to_be_clickable((By.ID, 'nc_1_n1z')))

# 拖动滑块验证
slider_bg = driver.find_element(By.ID,'nc_1__bg')
slider_width = slider.size['width']
slider_bg_width = slider_bg.size['width']
slider_offset_x = slider.location['x']
slider_bg_offset_x = slider_bg.location['x']
distance = slider_bg_offset_x - slider_offset_x + 5
ActionChains(driver).move_to_element_with_offset(slider, 5, 5).click_and_hold().perform()
time.sleep(0.5)
for i in range(6):
    ActionChains(driver).move_by_offset(distance/6, 0).perform()
    time.sleep(0.1)
ActionChains(driver).release().perform()


