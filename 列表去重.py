a_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
# 方法一
b_set = set(a_list)
a_list = list(b_set)
print(a_list)

#方法二
a_list = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7]
b_list=list()
for var in a_list:
    if var not in b_list:
        b_list.append(var)

print(b_list)
