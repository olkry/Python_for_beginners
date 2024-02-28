# Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два
# натуральных числа n и k и возвращает значение биномиального коэффициента

import math


# объявление функции
def compute_binom(n, k):
    return int((math.factorial(n)) / (math.factorial(k) * (math.factorial(n - k))))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
