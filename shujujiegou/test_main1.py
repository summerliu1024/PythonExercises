# from shujujiegou import test_main
#
# # test_main.test_fun()
#
#
# def main():
#     for i in range(100):
#         print(i)
#
# if __name__ == '__main__':
#     main()


# d = dict()
#
# d[1] = 5
# d[2] = 6
# d[3] = 7
# d[4] = 8
#
# a=list()
# for key in d.keys():
#     a.append(key)
#
# a.sort()
# print(a)
#
# for i in a:
#     print("{}:{}".format(i,d[i]))
#     print("%s:%s"%(i,d[i]))
#
#
#
# a={"a":4,"b":5,"c":2,"d":1}


# l=[]
# a={"num":0}
#
# for i in range(4):
#     a["num"]=i
#     l.append(a)
#
# print(l)
# print(a)

a = {"a": 4, "b": 5, "c": 2, "d": 1}

# list1=list()
# for i in a.values():
#     list1.append(i)
#
# print(list1)
#
# list1.sort()
# print(list1)
#
# for var in list1:
#     print()

# b = {}
# for k in a:
#     b[a[k]] = k
#
# l = list(b.values())
#
# l.sort()
#
# c = {}
#
# for i in l:
#     c[b[i]] = i
#
# print(c)
# a = {"a":4,"b":3,"c":2,"d":1}
# l = []
# b = {}
# for k in a:
#     b[a[k]] = k
# l = list(a.values())
# l.sort()
# c = {}
# for i in l:
#      c[b[i]]=i
# print(c)

# A = [1, 2, 3, 4, 5, 6]
#
# B = [4, 5, 6, 7, 8, 9, 10]
# c = set(A)
# d = set(B)
#
# print(c & d)
# print(c ^ d)
# print(c | d)

# a = {1: 2, 2: 3, 3: 5}
# print(sum(a.keys()))
# print(sum(a.values()))


a = {1: 2, 2: 3, 3: 5}
b = c = 0

# for i in a:
# for i in a.keys():
# for i in a.values():

for key, value in a.items():
    #dzgcdgkh
    b, c = b + key, c + value

#
print(b, c)
