# Write a program that takes an integer x and determines if the given number belongs to the given intervals.
#
# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')