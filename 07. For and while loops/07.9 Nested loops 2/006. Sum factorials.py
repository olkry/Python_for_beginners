# Дано натуральное число n. Напишите программу, которая выводит значение суммы 1!+2!+3!+...+n!.
import math
import time

number = int(input())
num_2 = number
total = 0
s_time = time.time()
while number > 0:
    factor = 1
    for i in range(1, number + 1):
        factor *= i
    total += factor
    number -= 1
e_time = time.time()

print(total)
print(e_time - s_time)

total = 0
s_time = time.time()
while num_2 > 0:
    total += math.factorial(num_2)
    num_2 -= 1
e_time = time.time()

print(total)
print(e_time - s_time)
