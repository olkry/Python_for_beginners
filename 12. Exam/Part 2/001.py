# На вход программе подается четное число n,n≥2. Напишите программу, которая выводит список четных чисел
numbers = []
for i in range(2, int(input()) + 1, 2):
    numbers.append(i)
print(numbers)
