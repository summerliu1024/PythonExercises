# def t1():
#    l = []
#    for i in range(10000):
#       l = l + [i]
# def t2():
#    l = []
#    for i in range(10000):
#       l.append(i)
# def t3():
#    l = [i for i in range(10000)]
# def t4():
#    l = list(range(10000))
#
# from timeit import Timer
#
# timer1 = Timer("t1()", "from __main__ import t1")
# print("concat ",timer1.timeit(number=100), "seconds")
# timer2 = Timer("t2()", "from __main__ import t2")
# print("append ",timer2.timeit(number=100), "seconds")
# timer3 = Timer("t3()", "from __main__ import t3")
# print("comprehension ",timer3.timeit(number=100), "seconds")
# timer4 = Timer("t4()", "from __main__ import t4")
# print("list range ",timer4.timeit(number=100), "seconds")
#


I = []

for i in range(4):
    I.append({"num": i})

print(I)

I = []
a = {"num": 0}

for i in range(4):
    a["num"] = i
    I.append(a)

print(I)
