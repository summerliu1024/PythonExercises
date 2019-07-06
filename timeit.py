import timeit

import os
def t1():
    li=[]
    for i in range(10000):
        li.append(i)


def t2():
    li=[]
    for i in range(10000):
        li=li+[i]

def t3():
    li=[i for i in range(10000)]

def t4():
    li=list(range(10000))


timer1=timeit.Timer("t1()",'from __main__ import t1')
timer2=timeit.Timer("t2()",'from __main__ import t2')
timer3=timeit.Timer("t3()",'from __main__ import t3')
timer4=timeit.Timer("t4()",'from __main__ import t4')


print("append:%f"%timer1.timeit(number=100))
print("[]+[]:%f"%timer2.timeit(number=100))
print("[i for]:%f"%timer3.timeit(number=100))
print("list():%f"%timer4.timeit(number=100))
