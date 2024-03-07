# Переведите двоичное число 111111 в десятичную систему счисления.

number_inp = 111111
greder = 0
num = 0

while number_inp > 0:
    number = number_inp % 10
    num += number * (2 ** greder)
    greder += 1
    number_inp //= 10

print(num)
