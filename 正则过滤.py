import re

a = "not 404 found 张三 99 深圳"
li = a.split(" ")
print(li)
res = re.findall('\d+|[a-zA-Z]+', a)  # \d匹配数字，|[]中匹配单词，+连接多个匹配方式
print(res)
for i in res:
    if i in li:
        li.remove(i)
new_str = " ".join(li)
print(res)
print(new_str)
