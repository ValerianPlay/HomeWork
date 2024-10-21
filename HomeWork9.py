first = input("Сюда число: ")
second = input("И сюда число: ")
third = input("Последнее: ")
if first != second != third and first != third:
    print(0)
elif first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(1)
