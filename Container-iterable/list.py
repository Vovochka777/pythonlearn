#  creation
l =  [1, 2, 3, 4, 5, 6, 7]
l2 = list([1, 'some', 3.5])
matrix = [[0, 1], [1, 2]]
zeros = [0] * 5

# access
#lastone = l[-1]  # 0 = first. -1 the last one  [-max possible, +max possible]
letters = ["a", "b", "c", "d"]
letters[0:3]  # "a", "b", "c"
letters[:3]  # "a", "b", "c"
letters[0:]  # "a", "b", "c", "d"
letters[:]  # "a", "b", "c", "d"
letters[::2]  # "a", "c"
letters[::-1]  # "d", "c", "b", "a"
first, second, *other = letters
print(first, second, other)

# insert
#l[0] = 2
#l.append(2)  # add to end
#l.insert(1, "777")  #Insert object before index. # 0 - add to first, 1 - to second, 99999 to last
#l.insert(len(l), "777")  # insert to last

#delete
#del l[-3] # index from 0 to maximum possible. -1 the last one. [-max possible, +max possible]
#l.pop(-8) #delete [-max possible, +max possible]
#l.remove(4) # remove value 4. Not index
l.pop() # delete last one

del l[0]

# Looping over lists
for letter in letters:
    ...

for index, letter in enumerate(letters):
    ...

l.count(1)  # count number of element 1
lcopy = l.copy()  # [1, 2, 3]
lcopy[0] = 777
lcopy2 = l[:]



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
list1.extend(list2)

del l[0]
l.clear()