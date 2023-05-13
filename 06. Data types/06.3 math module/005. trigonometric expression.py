# Write a program that calculates the value of the trigonometric expression sin x + cos x + tan² x
# by a given number of degrees x.
#   Trigonometric functions take an argument in radians. To convert degrees to radians, use the formula
# r = (x*π)/180
# The math module contains a built-in radians() function that converts an angle from degrees to an angle in radians.
#
# Напишите программу, вычисляющую значение тригонометрического выражения sin x + cos x + tan² x
# по заданному числу градусов x.
#  Тригонометрические функции принимают аргумент в радианах. Чтобы перевести градусы в радианы, воспользуйтесь формулой
# r = (x*π)/180
# Модуль math содержит встроенную функцию radians(), которая переводит угол из градусов в угол в радианах.

import math

degrees = math.radians(float(input()))
print(math.sin(degrees) + math.cos(degrees) + math.pow(math.tan(degrees), 2))
