def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    else:
        return True


# объявление функции
def get_next_prime(num):
    for number in range(num + 1, (num + 1) ** 2):
        if is_prime(number):
            return number
# ============================
# def get_next_prime(num):
#     cur_num = num + 1  # начинаем искать следующее простое число
#
#     while not is_prime(cur_num):  # если следующее число непростое, то увеличиваем на 1
#         cur_num += 1
#
#     return cur_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
