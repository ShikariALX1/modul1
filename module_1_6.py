my_dict = {'mark': 1995, 'alex': 2000}
print(my_dict)
print(my_dict.get('alex', 'max'))
my_dict.update({'ed': 1989, 'mel': 2001})
print(my_dict)
print(my_dict.pop('ed'))
print(my_dict)

my_set = {1, 1, 1, 2, 4, 1, 4, 2, 2, 3, (1, 2, 3), (1, 2, 3)}
my_set = set(my_set)
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.remove(1)
print(my_set)
