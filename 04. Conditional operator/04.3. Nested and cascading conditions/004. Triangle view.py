# Write a program that takes three positive numbers and determines the shape of a triangle,
# the lengths of the sides of which are equal to the entered numbers.
#
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.

shape_a, shape_b, shape_c = int(input()), int(input()), int(input())
if shape_a == shape_b and shape_b == shape_c and shape_a == shape_c:
    print('Равносторонний')
elif (shape_a != shape_b and shape_b != shape_c and shape_c != shape_a):
    print('Разносторонний')
else:
    print('Равнобедренный')
    