# Write a program that checks that for a given four-digit number the following
# relationship holds: the sum of the first and last digits is equal to the difference
# between the second and third digits.
#
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется
# следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.

num = int(input())
digit1 = num // 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')