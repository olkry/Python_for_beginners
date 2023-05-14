# The input to the program is a natural number n. Write a program that for each of the numbers from
# 0 to n (inclusive) prints the phrase: "The square of the number [number] is [number]" (without quotes).
#
# На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел от
# 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).


# for i in range(int(input())+1):
#     print(f'Квадрат числа {i} равен {i**2}')

[print(f'Квадрат числа {i} равен {i**2}') for i in range(int(input())+1)]
