#  work with copy()
# error

import pickle
from copy import copy, deepcopy

class A(object):
    def __init__(self):
        print('init')
        self.v = 10
        self.z = [2,3,4]

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

a = A()
a.v = 11
b1, b2 = copy(a), deepcopy(a)
a.v = 12
a.z.append(5)
print(b1.v, b1.z)
print(b2.v, b2.z)

