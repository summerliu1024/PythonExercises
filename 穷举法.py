import time
sta_time=time.time()
for a in range(0,1001):
    for b in range(0,1001):
        c=1000-a-b
        if (pow(a,2)+pow(b,2)==pow(c,2)):
                print(a,b,c)
end_time=time.time()

cost_time=end_time-sta_time

print("cost_time:%f"%cost_time)