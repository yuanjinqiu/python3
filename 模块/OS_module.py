import os
"""
os模块必会操作
os.path.join
os.path.basedir
os.path.abspath
os.path.basename
os.path.dirname
os.remove
os.rename
os.listdir
"""

# 将多个路径组合后返回
s = os.path.join('/home','jinqiu','data')
print(s)
#返回path最后的文件名
base = os.path.basename('/home/jinqiu/ip.py')
print(base)
##获取当前文件的绝对路径
abs = os.path.abspath('OS_module.py')
print(abs)
#返回path的目录
dirname = os.path.dirname('/Users/v_yuanjinqiu/python3/模块/OS_module.py')
print(dirname)
#如果path存在，返回True；如果path不存在，返回False
ex = os.path.exists('OS_module')
print(ex)

##将这个文件的绝对路径分成目录与文件，注意加r
sp = os.path.split('/Users/v_yuanjinqiu/python3/模块/OS_module.py')
print(sp[0],sp[1])