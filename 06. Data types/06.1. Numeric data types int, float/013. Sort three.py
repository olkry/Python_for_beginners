# Write a program that sorts three numbers from largest to smallest.
# The input to the program is three integers, each on a separate line.
#
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# На вход программе подается три целых числа, каждое на отдельной строке.

num1, num2, num3 = int(input()), int(input()), int(input())
print(max(num1, num2, num3), (num1 + num2 + num3) - max(num1, num2, num3) - min(num1, num2, num3),
      min(num1, num2, num3), sep='\n')
