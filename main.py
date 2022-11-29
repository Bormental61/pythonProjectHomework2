# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# my var строковое решение
# n = input('Введите вещественное число: ')
# summ = 0
# for i in n:
#     if i != '.' and i != ',':
#         summ += int(i)
# print(summ)

#var2 цифровое решение
# from decimal import Decimal
#
# b = Decimal(input("Введите число = "))
# sum = 0
# while b % 1 != 0:
#     b *= 10
# while b != 0:
#     sum = sum + int(b) % 10
#     b //= 10
# print(sum)

#_____________________________________________________
# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# n = int(input('Введите число: '))
# second_multy = 1
# print('[', end=' ')
# for i in range(1, n):
#     second_multy *= i
#     print(second_multy, end=', ')
# second_multy *= n
# print(second_multy, ']')

#____________________________________________________________
# 16. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# Для n = 4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9,06

# n = int(input('Ведите число: '))
# n_list = {}
# summ = 0
# for i in range(1, n + 1):
#     n_list[i] = (1 + 1 / i) ** i
#     summ += n_list[i]
# print('Сумма', round(summ, 2))

#_________________________________________________________________________
# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# import random
#
# n = int(input())
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
# with open('file.txt', 'r', encoding='utf-8') as file:
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)

# v2
# import random
# n = int(input())
# mult = 1
# some_list = [random.randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('file.txt', 'w+', encoding='utf-8') as file:
#     count = random.randint(1, n)
#     for _ in range(count):
#         file.write(f'{random.randint(0, n - 1)}' + '\n')
#     file.seek(0, 0)
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * some_list[int(index)]
# print(mult)


#____________________________________________________________________
# 18. Реализуйте алгоритм перемешивания списка.

# import random
# new_list = list(range(1, 100, 3))
# print(new_list)
# random.shuffle(new_list)
# print(new_list)

