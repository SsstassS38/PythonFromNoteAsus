# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# from decimal import Decimal
import random

list = []
values = 0
for i in range(5):
    values = round(random.uniform(0, 10), 2) 
    list.append(values)
min = list[0]
max = 0
for i in range(len(list)):
    
    if max < list[i]:
        max = list[i]
    if min > list[i]:
        min = list[i]
dif = (max - int(max)) - (min - int(min))

print(list)
print(max, min)
print(round(dif, 2))