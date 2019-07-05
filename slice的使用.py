s = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
#
a = slice(0, 11, 2)
print(a.indices(len(s)))


for i in range(*a.indices(len(s))):
    print(s[i])
