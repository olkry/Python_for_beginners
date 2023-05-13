# Write a program that calculates the value ⌈x⌉ +⌊x⌋ given a real number x.
#
# Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.

import math

number = float(input())
print(math.ceil(number) + math.floor(number))
