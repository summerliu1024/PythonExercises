a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn(a):
    return a % 2 == 1


li = filter(fn, a)

newli = list(li)  # 等价于 newli=[i for i in newli]

print(newli)

import math

# # 过滤出列表中的所有奇数：
# def is_odd(n):
#     return n % 2 == 1
#
#
# newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(newlist)
# for i in newlist:
#     print(i)
