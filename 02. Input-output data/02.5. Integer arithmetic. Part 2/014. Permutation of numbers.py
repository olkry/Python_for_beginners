# Given a three-digit number abc in which all digits are different.
# Write a program that prints the six numbers formed by permuting the digits of a given number.
#
# Дано трехзначное число abc в котором все цифры различны.
# Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

number = int(input())
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10
print(digit1, digit2, digit3, sep='')
print(digit1, digit3, digit2, sep='')
print(digit2, digit1, digit3, sep='')
print(digit2, digit3, digit1, sep='')
print(digit3, digit1, digit2, sep='')
print(digit3, digit2, digit1, sep='')