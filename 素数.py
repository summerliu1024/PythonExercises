#
# def is_prime(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     elif 0 not in [n % i for i in range(2, n)]:
#         return 1
#     else:
#         return 0
#
#
# result=filter(is_prime, range(1, 101))
#
# for i in result:
#     print(result)

list=[]
i=2
'''100可以替换为任何数字'''
for i in range (2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        list.append(i)
print(list)

