# The input to the program is a natural number n (n>=0) - the leg of a right-angled isosceles triangle.
# Write a program that prints a star triangle according to the example.
#
# На вход программе подается натуральное число n (n>=0) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звездный треугольник в соответствии с примером.


cathetus = int(input())
# for i in range(cathetus):
#     print('*' * (cathetus - i))

[print('*' * (cathetus - i)) for i in range(cathetus)]
