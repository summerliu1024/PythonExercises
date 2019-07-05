import time
a1 = time.time()
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if 1000 == a + b + c and a **2 + b **2 == c **2 :
                print(a,b,c)
a2 = time.time()
a3 = a2 - a1
print(a3)