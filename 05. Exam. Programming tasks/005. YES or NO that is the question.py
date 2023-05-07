# Write a program that takes a number as input and outputs the text "YES" or "NO" depending on the conditions.
# Conditions:
# if the number is odd, then output "YES";
# if the number is even in the range from 2 to 5 (inclusive), then output "NO";
# if the number is even in the range from 6 to 20 (inclusive), then output "YES";
# if the number is even and greater than 20, then output "NO".
#
# Напишите программу, которая принимает на вход число и в зависимости от условий выводит текст «YES», либо «NO».
# Условия:
# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».

x = int(input())
if x > 20 and x % 2 == 0:
    print('NO')
elif 6 <= x <= 20 and x % 2 == 0:
    print('YES')
elif 2 <= x <= 5 and x % 2 == 0:
    print('NO')
else:
    print('YES')
