# На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
#
# Формат входных данных
# На вход программе подается одно натуральное число.
#
# Формат выходных данных
# Программа должна вывести число записанное в двоичной системе счисления.

number = int(input())
string_numbers = ''

while number > 1:
    num = number % 2
    string_numbers = str(num) + string_numbers
    number //= 2
string_numbers = str(number) + string_numbers

print(string_numbers)

print('-------------')

result = ""

while number > 0:
    result = str(number % 2) + result
    number //= 2

print(result)
