# Write a program that finds the smallest and largest of five numbers.
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
# На вход программе подается пять целых чисел, каждое на отдельной строке.

num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())
print(f'Наименьшее число = {min(num1, num2, num3, num4, num5)}',
      f'Наибольшее число = {max(num1, num2, num3, num4, num5)}', sep='\n')
