# Three real numbers a, b, c are given. Write a program
# which finds the real roots of the quadratic equation ax² + bx + c = 0
# The program should print the real roots of the equation if they exist, or the text "No roots" otherwise.
# If the equation has two roots, then you should print them in ascending order.
#
# Даны три вещественных числа a, b, c. Напишите программу,
# которая находит вещественные корни квадратного уравнения ax² + bx + c = 0
# Программа должна вывести вещественные корни уравнения если они существуют или текст «Нет корней» в противном случае.
# Если уравнение имеет два корня, то следует вывести их в порядке возрастания.

import math

a, b, c = float(input()), float(input()), float(input())
d = math.pow(b, 2) - (4 * a * c)
if d < 0:
    print('Нет корней')
elif d > 0:
    x1 = ((-b + math.sqrt(d)) / (2 * a))
    x2 = ((-b - math.sqrt(d)) / (2 * a))
    print(min(x1, x2), max(x2, x1), sep='\n')
else:
    print((-1) * (b / (2 * a)))
