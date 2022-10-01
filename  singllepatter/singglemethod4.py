# Method Four：通过__new__ 方法实现
class Demo4:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Demo4, cls).__new__(cls)
        return cls._instance


c1 = Demo4()
c2 = Demo4()
print(id(c1))
print(id(c2))