import re

"""
正则表达式基本语法
. : 匹配任意字符（除了换行符 \n）。
^ : 匹配字符串的开始。
$ : 匹配字符串的结尾。
* : 匹配前一个字符0次或多次。
+ : 匹配前一个字符1次或多次。
? : 匹配前一个字符0次或1次。
[] : 匹配括号内的任意一个字符。
| : 或运算符，匹配两者之一。
() : 用于组合表达式。
"""
a='abscdE123456'
pattern = r"hello"
string = "hello world \nhello\njin hello"
#re.match

result = re.match(pattern, string)

#re.search
res = re.search(pattern,string)

#re.findall
r = re.findall('hello',string)


#re.sub 替换匹配项
p = r"world"
s = "hello world world"
replacement = "Python"
result = re.sub(p, replacement, s)



#re.compile
rc = re.compile("hello")
resu = rc.match(string)
print(resu.group())



