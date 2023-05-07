# Write a program to convert a time interval given in minutes to a value expressed in hours and minutes.
#
# Напишите программу для пересчёта величины временного интервала, заданного в минутах, в величину,
# выраженную в часах и минутах.

minutes = int(input())
hour = 60
print(minutes, 'мин - это', minutes // hour, 'час', minutes % hour, 'минут', end ='.')

