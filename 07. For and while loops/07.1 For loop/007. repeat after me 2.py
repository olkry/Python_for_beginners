# Write a program that reads one line of text and outputs 10 lines
# numbered from 0 to 9, each with a specified line of text.
#
# Напишите программу, которая считывает одну строку текста и выводит 10 строк,
# пронумерованных от 0 до 9, каждая с указанной строкой текста.

strng = input()

for i in range(10):
    print(i, strng)
