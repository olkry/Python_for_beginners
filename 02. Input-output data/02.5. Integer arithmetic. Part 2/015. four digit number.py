# Write a program to find the digits of a four digit number.
#
# Напишите программу для нахождения цифр четырёхзначного числа.

number = int(input())
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10
print('Цифра в позиции тысяч равна', digit1)
print('Цифра в позиции сотен равна', digit2)
print('Цифра в позиции десятков равна', digit3)
print('Цифра в позиции единиц равна', digit4)