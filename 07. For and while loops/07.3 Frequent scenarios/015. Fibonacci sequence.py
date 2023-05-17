# Напишите программу, которая считывает натуральное число n и выводит первые n чисел последовательности Фибоначчи.

num_i_1 = 1
num_i_2 = 1

for i in range(int(input())):
    if i + 1 < 3:
        print(1, end=' ')
    else:
        print(num_i_1 + num_i_2, end=' ')
        num_i_1, num_i_2 = num_i_2 + num_i_1, num_i_1

