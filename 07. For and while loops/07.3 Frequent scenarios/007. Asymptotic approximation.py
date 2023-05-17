# The input to the program is a natural number n. Write a program that evaluates the value of an expression
# (1+(1/2)+(1/3)+...+(1/n)) - log(n).
#
# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения
# (1+(1/2)+(1/3)+...+(1/n)) - log(n).

import math

number = int(input())
total = 0

for i in range(1, number + 1):
    total += (1 / i)
print(total - math.log(number))
