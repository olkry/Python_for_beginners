# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

largest1 = 0
largest2 = 0

for i in range(int(input())):
    number = int(input())
    if largest1 < number:
        largest2, largest1 = largest1, number
    if number > largest2 and number != largest1:
        largest2 = number

print(largest1, largest2, sep='\n')
