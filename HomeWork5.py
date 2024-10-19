immutable_var = 1, 2, 3, True, 'Jojo'
print(immutable_var)
#immutable_var [3] = False
#print(immutable_var)
   # Нельзя изменять отдельные элементы кортежа, можно изменить только список внутри него, допустим если бы он выглядел
#    так: immutable_var = ([1, 2, 3], True, False, 'ola')
mutable_list = ['i', '0', 'fgh', True, 1, 2, 3]
print(mutable_list)
mutable_list [0]  = 'asd'
mutable_list [-1] = 8888
mutable_list [3] = False
print(mutable_list)
