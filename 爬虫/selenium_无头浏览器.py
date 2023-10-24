from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
#无可视化
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#规避检测
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
#实例化
S = Service("./chromedriver_mac64/chromedriver")
web = webdriver.Chrome(service=S,options=option,chrome_options=chrome_options)

web.get('https://www.baidu.com/')

print(web.page_source)

web.quit()