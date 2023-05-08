# The input to the program is the number n - the number of dog years.
# Write a program that calculates the age of a dog in human years.
# Note. For the first two years, a dog year is 10.5 human years.
# After that, each year of the dog is equal to 4 human years.
#
# На вход программе подается число n – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.
# Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам.
# После этого каждый год собаки равен 4 человеческим годам.

age = float(input())
print(age * 10.5 if age <= 2 else 21 + (age-2)*4)
