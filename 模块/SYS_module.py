import sys

# 命令行参数List，第一个元素是程序本身路径   ***
# 可以将文件后的内容传递到文件中使用
# 后端代码放在linux服务器上运行，接收cmd方式调用，后边的参数会传递过来
# 需要在terminal或者cmd终端里运行！
print(sys.argv[-1])
# 返回Python解释器加载的路径，模块的搜索路径，初始化时使用PYTHONPATH环境变量的值  ******
# 自定义模块：先从sys.path里面去找
# 可以添加自定义模块的路径
print(sys.path)
# 获取Python解释程序的版本信息
print(sys.version)
# 返回操作系统平台名称
print(sys.platform)

# 退出！
# sys.exit()