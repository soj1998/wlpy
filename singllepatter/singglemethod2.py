# Method Two：通过装饰器实现

class Singleton(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name)


s = Singleton("Tom")


# Method Two：通过装饰器实现
def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class Demo2(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = Demo2(1)
a2 = Demo2(2)
print(id(a1))
print(id(a2))


# Method Two：通过装饰器实现
def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


@singleton
class Demo2(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = Demo2(1)
a2 = Demo2(2)
print(id(a1))
print(id(a2))

