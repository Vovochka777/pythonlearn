# reload attribute

class A(object):
    def __setattr__(self, name, value):
        value *= 2
        self.__dict__[name] = value
        # object.__setattr__(self, name, value)


a = A()
a.my_attr = 5
print a.my_attr  # 2
