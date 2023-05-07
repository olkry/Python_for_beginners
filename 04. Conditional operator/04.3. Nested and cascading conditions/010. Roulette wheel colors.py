# On the roulette wheel, the pockets are numbered from 0 to 36. Below are the colors of the pockets:
# pocket 0 green;
# for pockets 1 to 10, odd-numbered pockets are red, even-numbered pockets are black;
# for pockets 11 to 18, odd-numbered pockets are black, even-numbered pockets are red;
# for pockets 19 to 28, odd-numbered pockets are red, even-numbered pockets are black;
# for pockets 29 to 36, odd-numbered pockets are black, even-numbered pockets are red.
# Write a program that reads the number of a pocket and shows if that pocket is green,
# red or black. The program should display an error message if the user enters a number
# which lies outside the range from 0 to 36.
#
# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:
# карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым,
# красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число,
# которое лежит вне диапазона от 0 до 36.

x = int(input())
if x == 0:
    print('зеленый')
elif 1 <= x <= 10:
    print('черный' if x % 2 == 0 else 'красный')
elif 11 <= x <= 18:
    print('красный' if x % 2 == 0 else 'черный')
elif 19 <= x <= 28:
    print('красный' if x % 2 != 0 else 'черный')
elif 29 <= x <= 36:
    print('красный' if x % 2 == 0 else 'черный')
else:
    print('ошибка ввода')
