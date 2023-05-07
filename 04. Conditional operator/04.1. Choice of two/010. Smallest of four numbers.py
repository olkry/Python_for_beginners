# Write a program that determines the smallest of four numbers.
#
# Напишите программу, которая определяет наименьшее из четырёх чисел.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < b:
    x = a
else:
    x = b
if c < d:
    y = c
else:
    y = d
if x < y:
    print(x)
else:
    print(y)