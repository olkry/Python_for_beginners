# 3 lines are entered in random order.
# Write a program that finds out whether it is possible to
# construct an increasing arithmetic progression from the lengths of these strings.
#
# Вводятся 3 строки в случайном порядке.
# Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

num1, num2, num3 = len(input()), len(input()), len(input())
char_min, char_max = min(num1, num2, num3), max(num1, num2, num3)
average = (num1 + num2 + num3) - char_min - char_max

print('YES' if char_max - average == average - char_min else 'NO')
