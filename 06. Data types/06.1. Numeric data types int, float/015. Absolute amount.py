# Given five numbers a1,a2,a3,a4,a5 write a program that calculates the sum of their moduli
# The program takes five real numbers as input.
#
# Даны пять чисел a1,a2,a3,a4,a5 напишите программу, которая вычисляет сумму их модулей
# На вход программе подается пять действительных чисел

num1, num2, num3, num4, num5 = abs(float(input())), abs(float(input())), abs(float(input())), \
    abs(float(input())), abs(float(input()))
print(num1 + num2 + num3 + num4 + num5)