# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

# объявление функции
def print_digit_sum(num):
    sum_of_dig = 0
    while num != 0:
        sum_of_dig += num % 10
        num //= 10
    print(sum_of_dig)
    # ------------------------
    # print(sum(int(i) for i in str(num)))
    # --------------------------
    # z = []
    # for i in range(len(n)):
    #     z.append(int(n[i]))
    # print(sum(z))


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
