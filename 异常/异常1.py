try:
    num = int(input("num is:"))
    res = 2/num
except ValueError:
    print("TypeError")

except ZeroDivisionError:
    print("除0错误")
else:
    print(res)
finally:
    print("end")









