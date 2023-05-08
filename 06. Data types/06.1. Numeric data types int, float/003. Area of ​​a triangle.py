# Write a program that reads the lengths of two legs in a right triangle and prints its area.
#
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

legs_a, legs_b = float(input()), float(input())
print(0.5 * legs_a * legs_b)
