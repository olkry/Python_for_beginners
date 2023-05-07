# Write a program that reads an integer and then prints the next and previous integer with explanatory text.
# Напишите программу, которая считывает целое число, после чего на экран выводится следующее
# и предыдущее целое число с пояснительным текстом.

q = int(input())
# print("Следующее за числом", q, "число:", q + 1)
# print("Для числа", q, "предыдущее число:", q - 1)

print(f'Следующее за числом {q}, число: {q + 1}', f'Для числа {q}, предыдущее число: {q - 1}', sep='\n')