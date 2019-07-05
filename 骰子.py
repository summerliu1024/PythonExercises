import random

result = list()

for i in range(100000):
    #骰子1
    a = random.randint(1, 6)
    #骰子2
    b = random.randint(1, 6)
    result.append(a + b)
print(result)

result_dict = dict()

print(set(result))

for i in set(result):
    result_dict[i] = "{:.2%}".format(result.count(i) / 100000)

print(result_dict)
