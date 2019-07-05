class MyDict(dict):

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return self.setdefault(key, MyDict())


mydict = MyDict()
mydict.a = 1
mydict.b = 2
mydict.c.d = 3

print(mydict)
print(mydict.c)