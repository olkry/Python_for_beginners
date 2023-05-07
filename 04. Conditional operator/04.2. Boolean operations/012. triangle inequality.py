# Write a program that takes three positive numbers and determines if
# whether there exists a non-degenerate triangle with such sides.
#
# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.

a, b, c = int(input()), int(input()), int(input())
if a < b + c and b < a + c and c < a + b:
    print('YES')
else:
    print('NO')
