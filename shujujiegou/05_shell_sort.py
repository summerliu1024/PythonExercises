def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        # 插入排序算法
        for j in range(gap, n):
            # 处理元素向前遍历插入到相应的位置上
            i = j
            while (i-gap) >= 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap间隔
        gap //= 2


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    shell_sort(li)
    print(li)