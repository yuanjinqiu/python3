from time import sleep
from lxml import etree
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://www.taobao.com"

driver = webdriver.Firefox()
driver.get(url=url)
input_name = driver.find_element(By.ID,'q')
input_name.send_keys('手机')
sleep(3)
but = driver.find_element(By.CSS_SELECTOR,'.btn-search')
but.click()
sleep(10)

driver.quit()