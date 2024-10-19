my_dict = {'Kukold': 'Andrey', 'BodyBilder': 'Vasya'}
print(my_dict)
print(my_dict.get('Kukold'))
print(my_dict.get('BDSM', "Вот это замес!"))
my_dict.update({'Loli': 200, 'Popi': 300})
print(my_dict)
print(my_dict.pop('Kukold'))
print(my_dict)

my_set = {1,1,2,2,3,3,4,4,5,5,5,5,5,5}
print(my_set)
my_set.add(7)
my_set.add(10)
my_set.discard(3)
print(my_set)