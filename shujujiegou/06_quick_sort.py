def quick_sort(alist, start, end):
    """快速排序"""
    if start >= end:
        return
    mid = alist[start]
    left = start
    right = end

    # left与right未重合，就向中间移动
    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]
        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    # 从循环退出后，left与right相遇，即left==right
    alist[left] = mid

    # 对左边部分执行快速排序
    quick_sort(alist, start, left-1)

    # 对右边部分执行快速排序
    quick_sort(alist, left+1, end)

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)


