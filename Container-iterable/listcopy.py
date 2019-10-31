from copy import copy, deepcopy

'''
0 // common only with reference list (lstref = lst1). Copy create separate copy
1
    2.0 // common with reference list list and copy list. Deepcopy create separate copy
    2.1
        2.1.0
        2.1.1
    3.0
'''

lst1 = ['0','1',['2.0',['2.1.0','2.1.1'],'3.0']]
lstref = lst1
lst2 = copy(lst1)
lst3 = deepcopy(lst1)

lst1[0] = 'common value'

print("orig",lst1)
print("red",lstref)
print("copy",lst2)
print("deep",lst3)

lst1 = ['0','1',['2.0',['2.1.0','2.1.1'],'3.0']]
lstref = lst1
lst2 = copy(lst1)
lst3 = deepcopy(lst1)

lst1[2][0] = 'common value'
print('       ')
print("orig",lst1)
print("refe",lstref)
print("copy",lst2)
print("deep",lst3)
