# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
#
# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

# объявление функции
def number_of_factors(num):
    factors = [number for number in range(1, num + 1) if num % number == 0]
    return len(factors)
# -------------------------------
#     dividers_cnt = 1  # включаем сюда само число
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             dividers_cnt += 1
#
#     return dividers_cnt


# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))