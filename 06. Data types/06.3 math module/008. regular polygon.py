# A regular polygon is a convex polygon in which all sides and all angles between adjacent sides are equal.
# The area of a regular polygon with side length a and number of sides n is calculated by the formula:
# S = (n*a²)/(4*tg(π/n))
# Two numbers are given: a natural number n and a real number a.
# Write a program that finds the area of a given regular polygon.
#
# Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами.
# Площадь правильного многоугольника с длиной стороны a и количеством сторон n вычисляется по формуле:
# S = (n*a²)/(4*tg(π/n))
# Даны два числа: натуральное число n и вещественное число a.
# Напишите программу, которая находит площадь указанного правильного многоугольника.

from math import *

n, a = float(input()), float(input())

print((n*pow(a,2))/(4*(tan(pi/n))))
