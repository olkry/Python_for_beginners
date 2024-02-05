# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей
# и сумму его делителей. Если таких чисел несколько, то выведите наибольшее из них.
# Формат входных данных
# На вход программе подаются два числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести два числа на одной строке, разделенных пробелом:
# число с максимальной суммой делителей и сумму его делителей.


num_a = int(input())
num_b = int(input())
counter = 0
largest = 0

for i in range(num_a, num_b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
        if total >= counter:
            counter = total
            largest = i

print(largest, counter)
