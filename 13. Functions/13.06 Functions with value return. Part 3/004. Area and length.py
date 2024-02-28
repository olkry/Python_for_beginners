# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и
# возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.
import math


# объявление функции
def get_circle(radius):
    length_def = 2 * (math.pi * radius)
    square_def = math.pi * radius ** 2
    return length_def, square_def

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
