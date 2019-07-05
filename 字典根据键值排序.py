from collections import OrderedDict

dic = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
print(dic.items())
li = sorted(dic.items(), key=lambda i: i[0])
print('根据键排序：', li)
new_dic = OrderedDict(li)

print(new_dic)

for var in new_dic:
    print(var)
