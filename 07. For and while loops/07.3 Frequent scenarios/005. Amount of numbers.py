# The program receives two integers a and b (a≤b) as input. Write a program that counts the number of numbers in the range from
# a to b inclusive, whose cube ends in 4 or 9.
#
# На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от
# a до b включительно, куб которых оканчивается на 4 или 9.

num_a, num_b = int(input()), int(input())

count = 0
for i in range(num_a, num_b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1

print(count)
