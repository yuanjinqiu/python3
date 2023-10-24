#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : 爬虫-selenium-模拟登录古诗文网.py
# @Author: JinQiu
# @Date  : 2020/12/2

from lxml import etree
import requests
from selenium import webdriver
from time import sleep
from PIL import Image
from lxml import etree
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
web = webdriver.Firefox()
url = 'http://login.txgyhlw.com'
web.get(url=url)

sleep(3)

# 解析验证码地址

# 截图保存
web.save_screenshot('./yanzm/aa.png')

# 确定验证码图片对应的左上角和右下角的坐标
code_img_ele = web.find_element(By.XPATH,'/html/body/div[1]/div/table/tbody/tr/td[2]/div/div/div[3]/form/p[3]/a/img')
#/html/body/div[1]/div/table/tbody/tr/td[2]/div/div/div[3]/form/p[3]/a/img
location = code_img_ele.location
print(location, 'local')
# 验证码的长和宽
size = code_img_ele.size
print(size)
# 左上角和右下角的坐标
rangle = (
900, 200, 2100, 800
#int(location['x']), int(location['y']), int(location['x'] + size['width']),int(location['y'] + size['height'])
)
print(rangle)

# 裁剪图片

i = Image.open('./yanzm/aa.png')
code_img_name = './yanzm/code.png'

frame = i.crop(rangle)
frame.save(code_img_name)

chaojiying = Chaojiying_Client('18338671101', '18338671101', '946672')	#用户中心>>软件ID 生成一个替换 96001
im = open('./yanzm/code.png', 'rb').read()	    #本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
dic = chaojiying.PostPic(im, 1902)	#1902 验证码类型  2004中文类型 官方网站>>价格体系 3.4+版 print 后要加()
result = dic['pic_str']
print(result)

user_ipute = web.find_element(By.NAME,'username')
user_ipute.send_keys('zhouxi')

passwd_input = web.find_element(By.NAME,'password')
passwd_input.send_keys('Password01!')

sleep(3)
code_inpute = web.find_element(By.NAME,'captchaCode')
code_inpute.send_keys(result)
#
btn = web.find_element(By.ID,'submit-button')
btn.click()

sleep(2)
web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# web.get('http://console.txgyhlw.com/')
bur = web.find_element(By.CLASS_NAME,'header-title')
bur.click()


# tree = etree.HTML(page_text)
#
# con_list = tree.xpath('//*[@id="mainSearch"]/div[2]/div/div')
# for con in con_list:
#     conten = con.xpath('./a[1]/text()')
#     print(conten)
#
sleep(100)
web.quit()
