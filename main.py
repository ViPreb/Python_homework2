# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
import random

# number = input('Введите число: ')
# s = 0
# for i in number:
#     if i != '.':
#         s = s + int(i)
# print(s)

# Задача 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
# number = int(input('Введите число: '))
# my_list = []
# sum = 0
# for i in range(1, number + 1):
#     my_list.append((1 + 1 / i) ** i)
#     sum += my_list[i - 1]
# print(my_list)
# print(f'Сумма элементов равна {sum}')

# Задача 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
import random
number = int(input('Введите число: '))
my_list = []
print(f'Введите список из {number} элементов через Enter')
for i in range(0, number):
    my_list.append(input())
print(f'Исходный список {my_list}')
buffer = 0
for j in range(0, len(my_list)-1):
    k = random.randint(0, len(my_list)-1)
    buffer = my_list[i]
    my_list[i] = my_list[k]
    my_list[k] = buffer
print(f'Перемешанный список {my_list}')
