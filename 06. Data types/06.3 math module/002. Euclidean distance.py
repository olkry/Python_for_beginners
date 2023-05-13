# On a plane, the Euclidean distance between two points (x1;y1) and (x2;y2)
# defined as p = √(x1-x2)² + (y1-y2)²
# Write a program that determines the Euclidean distance between two points whose coordinates are given.
# The program receives four real numbers as input, each on a separate line - x1 y1 x2 y2.
#
# На плоскости евклидово расстояние между двумя точками (x1;y1) и (x2;y2)
# определяется так p = √(x1-x2)² + (y1-y2)²
# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
# На вход программе подается четыре вещественных числа, каждое на отдельной строке – x1 y1 x2 y2.

from math import *

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))
