# Задача 1. Профессор Тимур преподает вводный курс статистики и попросил вас написать программу, которую он мог бы
# использовать на занятиях для имитации бросания игральных кубиков.
# Программа должна случайным образом генерировать два числа в диапазоне от 1 до 6 и показывать их.
#
# Решение. Для генерации целых чисел мы будем использовать функцию randint():

# import random
#
# print('Бросаем кубики... ')
# print('Значения граней:')
# print(random.randint(1, 6))
# print(random.randint(1, 6))

# Задача 2. В интервью с профессором Тимуром вы выясняете, что он хотел бы использовать программу для имитации нескольких поочередных бросаний кубика.
#
# Решение. Будем использовать цикл while, который имитирует один бросок кубиков и затем спрашивает пользователя,
# следует ли сделать еще один бросок. Цикл будет повторяться до тех пор, пока пользователь отвечает "да", набирая букву "д":

# import random
#
# again = 'д'
# while again.lower() == 'д':
#     print('Бросаем кубики... ')
#     print('Значения граней:')
#     print(random.randint(1, 6))
#     print(random.randint(1, 6))
#     again = input('Бросить кубики еще раз? (д = да, н = нет): ')

# Задача 3. Профессор Тимур был так доволен написанным вами симулятором бросания кубиков, что попросил вас
# разработать еще одну программу. Он хотел бы иметь симулятор десятикратного поочередного подбрасывания монеты.
# Всякий раз, когда программа имитирует подбрасывание монеты, она должна случайным образом показывать "орла" или "решку".

# Решение. Мы можем сымитировать бросание монеты путем генерации случайного числа в диапазоне от 0 до 1.
# Для генерации целых чисел мы будем использовать функцию randint():

import random

for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')