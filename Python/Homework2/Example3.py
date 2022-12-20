#Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

# lst = [input('Введите список через разделитель-точку')]

import random

my_lst = []
for i in range(10):
    my_lst.append(random.randint(0, 100))
print(f'случайный список: {my_lst}')

newint = 0
reslst = []
for item in my_lst:
    newint = random(item)
    reslst.append(newint)


print(f' Перемешанный список: {reslst}') 






