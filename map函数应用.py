"""
列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
"""

my_list = [1, 2, 3, 4, 5]


def fn(x):
    return x ** 2


res = map(fn, my_list)
my_list = []
for i in res:
    my_list.append(i)

print(my_list)

my_list2 = [i for i in my_list if i > 10]

print(my_list2)

my_list3 = [2, 3, 4, 5, 6]
my_list4 = [1, 2, 3, 4, 5, 9]


def fn1(x, y):
    if not x:
        x = 0
    return x + y


my_list5 = []
for i in map(fn1, my_list3, my_list4):
    my_list5.append(i)

print(my_list5)

print("*" * 100)

my_list = [1, 2, 3, 4, 5]
my_list6 = [1, 2, 3, 4, 9,4]
# [2,4,6,8,14,4]
res_list=map(lambda a, b: a + b, my_list, my_list6)

res_list=list(res_list)
print(res_list)

# # def fn2(x):
# #     return x**2
#
# a=map(lambda x:x**2,my_list)
# a=list(a)
# print(a)


import random

a=random.random()
print(a)

print(random.uniform(1,10))

import re

my_str='<div class="nam">中国</div>'

res=re.match(r'<div class=".*">(.*?)</div>',my_str)
print(res.group(1))

a=511
assert(a<500)
