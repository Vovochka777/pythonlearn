from copy import deepcopy


class MyClass:
    deep = ['a','b',['ab','ba']]
    shallow = ['a','b',['ab','ba']]
    def __deepcopy__(self, memo):
        print('deep copying ...')
        my_copy = type(self)()
        memo[id(self)] = my_copy
        my_copy.deep = deepcopy(self.deep, memo)
        return my_copy


my_object = MyClass()
my_object_copy = deepcopy(my_object)

my_object.deep[2][0] = "change"
my_object.deep[2][0] = "shallow"
print(my_object.deep)
print(my_object_copy.deep)
print("")
print(my_object.shallow)
print(my_object_copy.shallow)