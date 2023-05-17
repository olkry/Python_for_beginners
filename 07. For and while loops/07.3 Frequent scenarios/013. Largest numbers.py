# На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

largest1 = 0
largest2 = 0
num_last = 0

for i in range(int(input())):
    number = int(input())
    if largest1 < number:
        largest1 = number
    if num_last < number and num_last != largest1:
        num_last = number
    if largest2 < num_last:
        largest2 = num_last
print(largest1, largest2, end='\n')
