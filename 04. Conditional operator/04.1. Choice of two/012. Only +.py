# Write a program that reads three numbers and calculates the sum of only positive numbers.
#
# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

a, b, c = int(input()), int(input()), int(input())
if 0 < a:
    x = a
else:
    x = 0
if 0 < b:
    y = b
else:
    y = 0
if 0 < c:
    z = c
else:
    z = 0
print(x + y + z)