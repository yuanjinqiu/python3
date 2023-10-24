import yaml

#yaml转为字典
yaml_string = """
name: Alice
age: 30
contact:
  email: alice@example.com
  phone: '123-456-7890'
"""
# data = yaml.safe_load(yaml_string)
# print(type(data))

# ##读取yaml转化为字典
# with open('data.yaml','r')as f:
#     data = yaml.safe_load(f)
#     print(data['name'])





#字典转为yaml
data = {'name': 'Alice', 'age': 30, 'contact': {'email': 'alice@example.com', 'phone': '123-456-7890'}}

yaml_string = yaml.dump(data)
print(type(yaml_string))

##字典转为yaml并写入文件
with open('data.yaml','w')as f:
     yaml.dump(data,f)










