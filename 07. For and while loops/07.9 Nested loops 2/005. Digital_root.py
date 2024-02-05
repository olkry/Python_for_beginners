# На вход программе подается натуральное число n.
# Напишите программу, которая находит цифровой корень данного числа.
# Цифровой корень числа n получается следующим образом: если сложить все цифры этого числа,
# затем все цифры найденной суммы и повторять этот процесс до тех пор,
# пока в результате не будет получено однозначное число (цифра),
# которое и называется цифровым корнем изначального числа.
# Формат входных данных
# На вход программе подается одно натуральное число.
# Формат выходных данных
# Программа должна вывести цифровой корень введенного числа.

number = int(input())

while number > 9:
    summa = 0
    while number > 0:
        last_digit = number % 10
        summa += last_digit
        number //= 10
    number = summa

print(number)


# while number > 9:
#     number -= 9
#
# print(number)