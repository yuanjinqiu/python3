from chaojiying import Chaojiying_Client

if __name__ == '__main__':
    chaojiying = Chaojiying_Client('18338671101', '18338671101', '946672')	#用户中心>>软件ID 生成一个替换 96001
    im = open('b.png', 'rb').read()	    #本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    dic = chaojiying.PostPic(im, 1902)	#1902 验证码类型  2004中文类型 官方网站>>价格体系 3.4+版 print 后要加()
    print(dic['pic_str'])