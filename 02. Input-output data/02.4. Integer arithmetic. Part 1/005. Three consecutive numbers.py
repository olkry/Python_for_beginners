# Write a program to display three consecutive numbers on the screen, each on a separate line.
# The first number is entered by the user, the remaining numbers are calculated in the program.
# Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
# Первое число вводит пользователь, остальные числа вычисляются в программе.

# num = int(input())
# print(num)
# print(num + 1)
# print(num + 2)

print(num := int(input('Введите число: ')), num + 1, num + 2, sep='\n')
