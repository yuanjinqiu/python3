import json

#dumps与loads
# dumps方法——将字典(主要)对象转换成字符串
dict1 = {
    "name": 'jin',
    "age": 30
}
print(type(dict1))
s1 = json.dumps(dict1)
print(s1)
print(type(s1))

# loads方法——将字符串转换成字典
s2 = '{"name": "jin", "age": 30}'
s3 = json.loads(s2)
print(s3)
print(type(s3))


#dump与load
#dump
#注意，手动在文件里写的话，文件里的键值如果是字符串的话必须用双引号！！！
# #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
json.dump(dict1,open('a.txt','a+'))

#Load
#load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
d = json.load(open('a.txt','r',encoding='utf8'))
print(d)
print(type(d))
