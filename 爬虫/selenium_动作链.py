from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
# 指定驱动
web = webdriver.Chrome(executable_path='./chromedriver_mac64/chromedriver')
# 发起请求
web.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

web.switch_to.frame('iframeResult')

div = web.find_element(By.ID,'draggable')

#d动作链
action = ActionChains(web)

action.click_and_hold(div)

for i in range(5):
    action.move_by_offset(17,0).perform()
    time.sleep(0.3)
action.release()
print(div)