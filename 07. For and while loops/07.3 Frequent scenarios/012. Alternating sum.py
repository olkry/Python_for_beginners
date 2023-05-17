# The input to the program is a natural number n. Write a program to calculate the alternating sum
# 1-2+3-4+5-6...+(-1)**(n+1)*n.
#
# На вход программе подается натуральное число n. Напишите программу вычисления знакочередующей суммы
# 1-2+3-4+5-6...+(-1)**(n+1)*n.

number = int(input())

total = 0

for i in range(1, number + 1):
    if i % 2 != 0:
        total += i
    else:
        total -= i

print(total)
