# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
#
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
#
# Примечание. Гарантируется, что основание треугольника – нечетное число.


# объявление функции
def draw_triangle(fill, base):
    for i in range(base):
        print(fill * (i + 1) if i < base // 2 + 1 else fill * (base - i))
        # ------------------------------------
        # if i < base // 2 + 1:
        #     print(fill * (i + 1))
        # else:
        #     print(fill * (base - i))
        # --------------------------------------
        # for i in range(base // 2):
        #     print(fill * (i + 1))
        #
        # for i in range(base // 2, -1, -1):
        #     print(fill * (i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
