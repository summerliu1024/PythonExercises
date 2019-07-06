def Test(a, b):
    result = 0
    my_list = [a, b]
    my_list.sort()

    if my_list[0] == my_list[1]:
        if my_list[0] % 2 == 0:
            result = my_list[0] * 2
            return result
        else:
            return result

    else:
        # 此处考虑包含区间最后一个数字，不考虑可以不用加1
        for i in range(my_list[0], my_list[1] + 1):
            if i % 2 == 0:
                result += i
        return result


if __name__ == '__main__':
    result = Test(5, 10)
    print(result)
