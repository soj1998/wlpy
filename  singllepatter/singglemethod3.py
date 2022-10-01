#  Method Three：通过使用类实现

class Demo3(object):
    # 静态变量
    _instance = None
    _flag = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Demo3._flag:
            Demo3._flag = True


b1 = Demo3()
b2 = Demo3()
print(id(b1))
print(id(b2))

