from time import sleep
from lxml import etree
from selenium.webdriver.common.by import By

from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(5)
def scan_login(url):
    driver.get(url)
    # 等待扫码登录
    sleep(3)
    # 进入之后开始其他操作

    input_name = driver.find_element(By.ID, 'q')
    input_name.send_keys('手机')

    but = driver.find_element(By.CLASS_NAME,'btn-search')
    but.click()


    sleep(100)


    #登录后页面
    driver.quit()


if __name__ == '__main__':
    url = 'https://login.taobao.com/member/login.jhtml'
    scan_login(url)
