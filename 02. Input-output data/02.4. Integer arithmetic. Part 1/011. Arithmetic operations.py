# Write a program that calculates the sum, difference, and product of two integers entered from the keyboard.
# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.

num1 = int(input())
num2 = int(input())
# print(num1, '+', num2, '=', num1 + num2)
# print(num1, '-', num2, '=', num1 - num2)
# print(num1, '*', num2, '=', num1 * num2)

print(f'{num1} + {num2} = {num2+num1}', f'{num1} - {num2} = {num1-num2}',
      f'{num1} * {num2} = {num2*num1}', sep='\n')
