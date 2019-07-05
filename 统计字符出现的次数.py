from collections import Counter

a = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
res = Counter(a)
print(res)
for key, value in res.items():
    print("%s:%s" % (key, value))
