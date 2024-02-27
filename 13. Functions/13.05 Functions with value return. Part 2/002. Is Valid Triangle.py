# объявление функции
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        return True
    else:
        return False

# def is_valid_triangle(side1, side2, side3):
#     sides = sorted([side1, side2, side3])  # создаём отсортированный список из сторон
#
#     return sides[0] + sides[1] > sides[2]  # проверяем, минимальная и средняя стороны больше максимальной
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
