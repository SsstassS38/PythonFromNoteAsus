# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# a = int(input())
# f = bin(a)
# print(f)


n = int(input('Введите число: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)