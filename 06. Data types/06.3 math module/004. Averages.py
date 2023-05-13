# In mathematics, the following averages are distinguished:
# arithmetic mean of numbers a and b:(a+b)/2
# geometric mean of numbers a and b: √(a*b)
# harmonic mean of numbers a and b: (2*a*b)/(a+b)
# root mean square of numbers a and b: √(a²+b²)/2
# The input to the program is two real numbers a and b, each on a separate line.
# The program should display 4 numbers - the arithmetic mean, geometric mean, harmonic and quadratic.
#
# В математике выделяют следующие средние значения:
# среднее арифметическое чисел a и b:(a+b)/2
# среднее геометрическое чисел a и b: √(a*b)
# среднее гармоническое чисел a и b: (2*a*b)/(a+b)
# среднее квадратичное чисел a и b: √(a²+b²)/2
# На вход программе подается два вещественных числа a и b, каждое на отдельной строке.
# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

import math

num_a, num_b = float(input()), float(input())

print((num_a + num_b) / 2, math.sqrt(num_a * num_b), (2 * num_b * num_a) / (num_a + num_b),
      math.sqrt((math.pow(num_a, 2) + math.pow(num_b, 2)) / 2), sep='\n')
