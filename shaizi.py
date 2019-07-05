# -*- coding:utf-8 -*-
"""生成的文件用谷歌浏览器打开即可看到结果"""


import pygal
from random import randint

# 创建Die类
class Die():
    # 表示一个骰子的类
    def __init__(self, num_sides=6):
        # 骰子默认为6面
        self.num_sides = num_sides

    def roll(self):
        # 返回一个位于1和骰子面数之间的随机值
        return randint(1, self.num_sides)


# 创建三个D6骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 将结果存储在一个列表中
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling three D6 1000 time.'
hist.x_labels = ['3', '4', '5', '6', '7', '8',
                 '9', '10', '11', '12', '13', '14',
                 '15', '16', '17', '18']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

# add传递到图标，这种文件的扩展名必须为.svg  需要用谷歌浏览器打开才能查看
hist.add('D6 + D6 +D6', frequencies)
hist.render_to_file('D6_D6_D6.svg')
