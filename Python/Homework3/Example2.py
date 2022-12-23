#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


import random

lenth = int(input('Введите размер списка '))
listIn = []
listRes = []

for i in range(lenth):
    listIn.append(random.randint(0, 9))

for i in range(len(listIn)):
    while i < len(listIn)/2 and lenth > len(listIn)/2:
        lenth = lenth - 1
        prod = listIn[i] * listIn[lenth]
        listRes.append(prod)
        i += 1

print(listIn)
print(listRes)