import pprint
names = {'id1': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}},
       'id2': {'name': 'Mark', 'class': 2, 'subjects': {'Geometry', 'Java', 'Cooking'}},
       'id3': {'name': 'Ruslan', 'class': 1, 'subjects': {'Math', 'Algorithms', 'English'}}}
del names['id3']
pprint.pprint(names)
