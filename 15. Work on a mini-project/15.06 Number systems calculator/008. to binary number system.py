# Переведите десятичное число 513 в двоичную систему счисления.

number = 513
system = 2
answer = ''

while number >= system:
    last = number % system
    answer += str(last)
    number = int((number - last) / system)
answer += str(int(number))

print(answer[::-1])
