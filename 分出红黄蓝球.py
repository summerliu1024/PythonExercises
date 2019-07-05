from collections import Counter, OrderedDict

ball = ["a", "b", "c", "b", "a", "c", "b", "a", "c","e"]
ball_counts = Counter(ball)
print(ball_counts.elements())
for i in ball_counts.elements():
    print(i)
# 分组排序
print("分组",sorted(ball_counts.elements()))
# 去重
print("去重",sorted(ball_counts))
# 统计
print("不按顺序统计",ball_counts)

#有序字典
d = OrderedDict()
# d["a"]=ball_counts['a']
# d['b']=ball_counts['b']
# d['c']=ball_counts["c"]

for var in sorted(ball_counts):
    d[var]=ball_counts[var]

print(d)
#按顺序输出不同球对应的数量
for m, n in d.items():
    print(m, n)
