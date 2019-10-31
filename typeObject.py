o = object()
b = object()
class c:
    pass
d = c()


class C:
    pass



test = C

print ('is it object: ' + str( isinstance(test, object) ))
print ('is it type: ' + str(  isinstance(test, type) ))
print ('is object subclass: ' + str(  issubclass(test, object) ))

print (type(test))
#print  '__class__: ' + str(test.__class__ )

print  ('__bases__: ' + str(test.__bases__ ))



# http://www.cafepy.com/article/python_types_and_objects/
# Everything is object

# type and object are primitive objects in Python. We might as well have introduced them one at atime but that would lead to the chicken and egg problem - which to introduce first?
#print   isinstance(type, object)
#print   isinstance(object, type)

# There are only two kinds of objects in Python: to be unambiguous let's call these types and non-types.

# Types and classes are really the same in Python. Class is Type is Class
# type() function and the __class__ attribute get you the same thing.

# Non-types are concrete values so it does not make sense for another object be a subclass.
# Two good examples of objects that are not types are the integer 2 and the string "hello".

# Types and  non-types are both objects but only types can have subcasses. Hmm.. what does it mean to be a subclass of 2?
# If an object is an instance of <type 'type'>, then it is a type. Otherwise, it is not a type.

# This changes was implemented in  Python >= 2.3.
# That's why class declaration changed in  2.3 >=  Python < 3

# OLD class C: pass
# NEW class C(object): pass
# in Python 3 class C: pass

#Type(Class) with parethesis () create new object
# o = object()
# cobj = C()



