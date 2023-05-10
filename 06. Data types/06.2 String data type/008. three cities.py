# The names of three cities are given. Write a program that determines the shortest and longest city names.
# The input to the program is the names of three cities, each on a separate line.
#
# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# На вход программе подаётся названия трех городов, каждое на отдельной строке.

city1, city2, city3 = input(), input(), input()
city_char1, city_char2, city_char3 = len(city1), len(city2), len(city3)
print(city1 if min(city_char1, city_char2, city_char3) == city_char1
      else city2 if min(city_char1, city_char2, city_char3) == city_char2 else city3,
      city1 if max(city_char1, city_char2, city_char3) == city_char1
      else city2 if max(city_char1, city_char2, city_char3) == city_char2 else city3,
      sep='\n')
