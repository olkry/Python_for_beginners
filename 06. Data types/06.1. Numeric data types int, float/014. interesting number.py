# We call a number interesting if it contains the difference between the maximum and minimum digits
# equals the average value. Write a program
# which determines whether the number is interesting or not. If the number is interesting
# should be output - "Number of interesting" otherwise "Number of uninteresting".
# The input to the program is a three-digit integer.
#
# Назовем число интересным, если в нем разность максимальной и минимальной цифры
# равняется средней по величине цифре. Напишите программу,
# которая определяет интересное число или нет. Если число интересное,
# следует вывести – «Число интересное» иначе «Число неинтересное».
# На вход программе подается целое трехзначное число.

number = int(input())
print('Число интересное' if max(number // 100, number // 10 % 10, number % 10) -
                            min(number // 100, number // 10 % 10, number % 10) ==
                            number // 100 + number // 10 % 10 + number % 10 -
                            max(number // 100, number // 10 % 10, number % 10) -
                            min(number // 100, number // 10 % 10, number % 10) else 'Число неинтересное')
