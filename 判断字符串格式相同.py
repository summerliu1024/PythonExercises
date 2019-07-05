from collections import Counter
from itertools import groupby
from collections import OrderedDict

a = "abcb"
b = "cdde"

a_list = list()
b_list = list()
a_dict = OrderedDict()
b_dict = OrderedDict()
# 先按照原字符串分组并计数，将结果保存到一个有序字典里面
for var, items in groupby(a):
    word_a = Counter(items)
    a_dict.update(word_a)

# 先按照原字符串分组并计数，将结果保存到一个有序字典里面
for var, items in groupby(b):
    word_b = Counter(items)
    b_dict.update(word_b)
# 再将结果里面统计的字符数量取出来保存到一个列表
for key, value in a_dict.items():
    a_list.append(value)
# 再将结果里面统计的字符数量取出来保存到一个列表
for key, value in b_dict.items():
    b_list.append(value)
# 两个列表如果相等，字符串格式必相等
if a_list == b_list:
    print("True")
else:
    print("False")
