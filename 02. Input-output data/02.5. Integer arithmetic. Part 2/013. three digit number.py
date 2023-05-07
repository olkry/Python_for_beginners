# Write a program that calculates the sum and product of the digits of a positive three-digit number.
#
# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

number = int(input())
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10
print('Сумма цифр', digit1 + digit2 + digit3, sep=' = ')
print('Произведение цифр', digit1 * digit2 * digit3, sep=' = ')