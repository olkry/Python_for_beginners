# Write a program that calculates the volume of a cube
# and its total surface area, given the value of the length of the edge.
# Напишите программу, вычисляющую объём куба
# и площадь его полной поверхности, по введённому значению длины ребра.

q = int(input())
v = q**3
s = 6*q**2
print("Объем =", v)
print("Площадь полной поверхности =", s)