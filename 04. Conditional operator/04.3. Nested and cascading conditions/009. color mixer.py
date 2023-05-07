# Red, blue and yellow are called primary colors,
# because they cannot be obtained by mixing other colors.
# When two primary colors are mixed, a secondary color is obtained:
# if you mix red and blue, you get purple;
# if you mix red and yellow, you get orange;
# If you mix blue and yellow, you get green.
# Write a program that reads the names of two primary colors to blend.
# If the user enters anything other than "red", "blue", or "yellow",
# then the program should display an error message.
# Otherwise, the program should display the name of the secondary color that will be the result.
#
# Красный, синий и желтый называются основными цветами,
# потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый»,
# то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

a, b = input(), input()
if a == b and (a == 'красный' or a == 'желтый' or a == 'синий'):
    print(a)
elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
    print('фиолетовый')
elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
    print('оранжевый')
elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
    print('зеленый')
else:
    print('ошибка цвета')
