def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    # 外层循环控制从头走到尾的次数
    for j in range(n-1):
        # j [0, 1,2,...n-2]
        #n-2-j
        count = 0
        # 内层循环控制从头走到尾的遍历
        for i in range(0, n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        #最优情况
        if 0 == count:
            break

if __name__ == '__main__':
    li = [54, 26, 77, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

#最坏时间 复杂度 O(n^2)
#最优时间 复杂度 O(n)
#算法稳定
    # [17, 20, 26, 31, 44, 54, 55, 77, 93]
