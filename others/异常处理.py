"""
try:
    #执行代码
except:
    #发生异常执行代码
except:
else:
    #没有异常时执行的代码
finally:
    #不管有没有异常都会执行的代码
"""


try:
    num = int(input('请输入一个整数：'))
    result = 10/num
except:
    #发生异常执行代码
    print('输入类型不对')
else:
    print(result)
finally: #无论有没有异常都输出
    print('ok')








