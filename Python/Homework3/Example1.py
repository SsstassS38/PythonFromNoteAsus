# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_lst = []
for i in range(5):
    my_lst.append(random.randint(0, 10))
print(f'случайный список: {my_lst}')
sum = 0
lenth = len(my_lst)
for i in range(lenth):
    if i%2 == 1:
        sum += my_lst[i]
print(f'сумма чисел на нечетных позициях списка: {sum}')



# my_list = [8, 5, 7, 3, 6]
# print(sum(my_list[1::2]))