# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c –
# коэффициенты квадратного уравнения ax**2+bx+c=0 и возвращает его корни в порядке возрастания.


# объявление функции
def solve(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x1_def = (-b + discriminant ** 0.5) / (2 * a)
    x2_def = (-b - discriminant ** 0.5) / (2 * a)
    return min(x1_def, x2_def), max(x1_def, x2_def)


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
