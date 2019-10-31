from array import array

my_list = [1, 'some', 3.5]  # change
my_tuple = 1, 'some', 3.5  # то же, что и (1, 'some', 3.5)
my_range = range(5)
my_str = 'а внутри "можно" поместить обычные скобки'
my_array = array('i', [1, -2, 15, 128])  # change
my_dict = {
        'key': 'value',
        'sub_dict': {},
        2: [1, 2, 3, 4],
    }

# change
my_list[0] = 777
my_array[0] = 777
my_dict["key"] = 777
