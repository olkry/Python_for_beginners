# Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10

# объявление функции
def draw_box():
    print('*' * 10)
    for _ in range(12):
        print('*', ' ' * 6, '*')
    print('*' * 10)

# основная программа
draw_box()  # вызов функции

def draw_box():
    print("*" * 10)

    for i in range(12):
        print("*", "*", sep=" " * 8)

    print("*" * 10)

draw_box()  # вызов функции