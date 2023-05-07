# Write a program that determines whether three given numbers (in the given order)
# are consecutive members of an arithmetic progression.
#
# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке)
# последовательными членами арифметической прогрессии.

a, b, c = int(input()), int(input()), int(input())
if (b - a) + b == c:
    print('YES')
else:
    print('NO')