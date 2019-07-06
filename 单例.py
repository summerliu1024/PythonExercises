class Singleton(object):
    __inited = None
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if Singleton.__inited:
            return
        print("初始化")
        Singleton.__inited=True

class MyClass(Singleton):
    a = 1


one = MyClass()
print(one)
two = MyClass()
print(two)