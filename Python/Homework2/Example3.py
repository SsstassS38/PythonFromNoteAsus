#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int


import random

my_lst = []
for i in range(5):
    my_lst.append(random.randint(0, 100))
print(f'случайный список: {my_lst}')

for i in range(len(my_lst)-1, 0, -1):
    j = random.randint(0, i - 1)
    my_lst[i], my_lst[j] = my_lst[j], my_lst[i]

print(f'Перемешанный список: {my_lst}') 

