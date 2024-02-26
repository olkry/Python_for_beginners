# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и
# возвращающую список всех делителей данного числа.


# объявление функции
def get_factors(num):
    factors = [number for number in range(1, num + 1) if num % number == 0]
    # -------------------------
    # factors.append(number for number in range(num) if num % number == 0)
    return factors
    # ------------------------
    # dividers = []
    # for i in range(1, num // 2 + 1):
    #     if num % i == 0:
    #         dividers.append(i)
    #
    # dividers.append(num)
    # return dividers

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))