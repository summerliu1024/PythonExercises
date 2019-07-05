import timeit


def way1():
    mylist = [i * i for i in range(1000)]
    n = 0
    for i in range(10000):
        if i in mylist:
            n += 1

        else:
            n += i * 2

    return n


def way2():
    myset = {i * i for i in range(1000)}
    n = 0
    for i in range(10000):
        if i in myset:
            n += 1

        else:
            n += i * 2

    return n


if __name__ == '__main__':
    t1=timeit.timeit("way1()",setup="from __main__ import way1",number=10)
    print(t1)

    t2 = timeit.timeit("way2()", setup="from __main__ import way2", number=10)
    print(t2)

    print(t2-t1)