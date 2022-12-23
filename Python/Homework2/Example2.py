#Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input('Введите число n: '))
my_list = list[n]
my_listRes =[]
res = 0
for i in range(0, n):
    res = round((1 + (1 / (i+1)))** (i+1), 2)
    my_listRes.append(res)
print(f'Последовательность для n={n}: {my_listRes}')
res2 = sum(my_listRes)
print(f'Сумма чисел последовательности: {res2}')


# 2 вариант решения задачи (оптимизация кода).
# n = int(input('Введите дробное число: '))
# lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]     #  видимо генератор..
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')
