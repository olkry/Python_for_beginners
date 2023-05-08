# Write a program that reads one number from the keyboard and prints its inverse.
# If the number entered from the keyboard is zero,
# then output "Reciprocal number does not exist" (without quotes).
#
# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль,
# то вывести «Обратного числа не существует» (без кавычек).

number = float(input())
print('Обратного числа не существует' if number == 0 else number ** -1)
