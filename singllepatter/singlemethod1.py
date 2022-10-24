# 1、通过导入模块实现

class Singleton(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name)


s = Singleton("Tom")


def show_method_one():
    """

    :return:
    """
    s1 = Singleton
    s2 = Singleton
    print(s1)
    print(s2)
    print(id(s1))
    print(id(s2))


show_method_one()

