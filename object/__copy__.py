from copy import copy

class SubClass:
    a = 5
    pass

class MyClass:
    sc = ['a','b',['ab','ba']]

    def fu(self):
        pass


my_object = MyClass()
my_object_copy = copy(my_object)

print(id(my_object.sc))
print(id(my_object_copy.sc))


