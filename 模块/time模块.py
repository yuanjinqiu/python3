import time

#时间戳(time.time)
print(time.time())
#结构化时间(time.localtime)
print(time.localtime())
#字符串时间(time.strftime)
"""
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%x 本地相应的日期表示
%X 本地相应的时间表示
"""
print(time.strftime('%Y-%m-%d %H:%M:%S'))




'''
    字符串时间————>结构化时间 strptime()
    结构化时间————>时间戳     mktime()
    时间戳    ————>结构化时间 localtime()
    结构化时间————>字符串时间 strftime()
'''


### 注意：
#  strftime('格式','结构化时间')  格式可以少写
#  strfptime('字符串时间','格式')  格式必须跟字符串时间一一对应！
