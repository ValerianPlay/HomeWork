grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
print(students)
name = {}
avg = sum(grades [0]) / len(grades [0])
name [students [0]] = avg
avg = sum(grades [1]) / len(grades [1])
name [students [1]] = avg
avg = sum(grades [2]) / len(grades [2])
name [students [2]] = avg
avg = sum(grades [3]) / len(grades [3])
name [students [3]] = avg
avg = sum(grades [4]) / len(grades [4])
name [students [4]] = avg
print(name)

# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students = list(students)
# students.sort()
# name = {}
# for i in range (len(students)):
#     avg = sum(grades[i]) / len(grades[i])
#     name [students [i]] = avg
# print(name)