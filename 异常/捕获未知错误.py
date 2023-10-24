try:
    num = int(input("num is:"))
    res = 2/num
# except ValueError:
#     print("value error")
except Exception as r :
    print("未知错误：%s" %r)
else:
    print(res)
finally:
    print("是否异常都会输出")

print("#"*10)