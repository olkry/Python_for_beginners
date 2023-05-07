# Write a program that reads two integers a and b and displays the square of
# the sum (a+b)^2 and the sum of the squares a^2+b^2 of these numbers.
#
# Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат
# суммы (a+b)^2 и сумму квадратов a^2+b^2 этих чисел.

num1 = int(input())
num2 = int(input())
print('Квадрат суммы', num1, 'и', num2, 'равен', (num1 + num2) ** 2)
print('Сумма квадратов', num1, 'и', num2, 'равна', num1 ** 2 + num2 ** 2)