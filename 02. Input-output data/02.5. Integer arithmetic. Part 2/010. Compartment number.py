# The compartment car has 9 compartments with four seats for passengers in each.
# Write a program that determines the number of the compartment in which the seat
# with the given number is located (numbering of seats is through, starts from 1)
#
# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
# Напишите программу, которая определяет номер купе, в котором находится место
# с заданным номером (нумерация мест сквозная, начинается с 1)


place = int(input())
print((place + 3) // 4)
