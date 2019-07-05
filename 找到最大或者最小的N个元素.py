
import heapq

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda x: x['shares'])


expensive = heapq.nlargest(3, portfolio, key=lambda a: a['price'])

print(cheap)
print(expensive)


a=[(1,2),(2,3),(4,5677),(8,89)]

c=sorted(a,key=lambda x:x[1])
print(c)


