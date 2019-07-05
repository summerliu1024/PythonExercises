s = "ajldjlajfdljfddd"
s1 = set(s)
s2 = list(s1)
s2.sort()
res = "".join(s2)
print(res)

s = lambda a, b: a * b
print(s(2, 4))
