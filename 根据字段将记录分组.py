rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]

from operator import itemgetter
from itertools import groupby

# 排序
rows.sort(key=itemgetter('date'))

print(1111,rows)
#
for var in groupby(rows, key=itemgetter("date")):
    print(var)

# 分组
for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print(" ", i)


#另外一种方法

from collections import defaultdict

#键是date 值是列表，列表里面的元素是date相同的元素
rows_by_date=defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)

#按照指定时间查询
for r in rows_by_date["07/01/2012"]:
    print(r)