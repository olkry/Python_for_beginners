# The famous American writer Ray Bradbury has a novel Fahrenheit 451.
# Write a program that determines what temperature on the Celsius scale
# corresponds to the specified Fahrenheit value.
# Use the conversion formula: C=(5/9)*(F-32)#

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту».
# Напишите программу, которая определяет, какой температуре по шкале Цельсия
# соответствует указанное значение по шкале Фаренгейта.
# Используйте формулу для перевода: C=(5/9)*(F-32)

fahrenheit = float(input())
print((5 / 9) * (fahrenheit - 32))
