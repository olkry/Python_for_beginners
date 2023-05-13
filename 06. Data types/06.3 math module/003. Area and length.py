# Write a program that determines the area of a circle and the circumference of a circle given a given radius R.
# The input to the program is one real number R
#
# S = πR²; C = 2πR;
#
# Напишите программу определяющую площадь круга и длину окружности по заданному радиусу R.
# На вход программе подается одно вещественное число R
#
# S = πR²;   C = 2πR;

import math

radius = float(input())
print(math.pi * math.pow(radius, 2), 2 * math.pi * radius, sep='\n')
