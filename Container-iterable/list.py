l = [1, 'some', 3.5]
l2 = list([1, 'some', 3.5])

del l[0]
l[0] = 2
l.reverse()
l.append(2)
l.reverse()
print(l)
l.count(1)  # count number of element 1
lcopy = l.copy()  # [1, 2, 3]
lcopy[0] = 777
lcopy2 = l[:]
print(l)
print(lcopy)
print(lcopy2)





del l[0]
l.clear()