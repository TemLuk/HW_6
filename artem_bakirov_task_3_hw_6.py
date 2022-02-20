my_dict = {1: 'one', 3: 'three', 5: 'five', 4: 'four', 2: 'two'}
list_keys = list(my_dict.keys())
list_keys.sort()
for i in list_keys:
    print(i, ':', my_dict[i])