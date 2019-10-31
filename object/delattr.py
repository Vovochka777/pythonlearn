# Класс определен в нотации Python 3.
class A():

    def __init__(self):
        self.data = ['el1', 'el2', 'el3']

    def __delattr__(self, name):
        self.data.remove(name)


a = A()
a.data  # ['el1', 'el2', 'el3']

del a.el2
a.data  # ['el1', 'el3']