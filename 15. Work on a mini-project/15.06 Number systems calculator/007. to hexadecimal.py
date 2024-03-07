# Переведите десятичное число 1000 в шестнадцатеричную систему счисления.

number = 1000
system = 16
answer = ''

while number >= system:
    last = number % system
    if last == 10:
        answer += 'A'
    elif last == 11:
        answer += 'B'
    elif last == 12:
        answer += 'C'
    elif last == 13:
        answer += 'D'
    elif last == 14:
        answer += 'E'
    elif last == 15:
        answer += 'F'
    else:
        answer += str(last)
    number = (number - last) / system
answer += str(int(number))

print(answer[::-1])

# ====================
n = int(input())
a = []
p = int(input())
digits = ['0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
while n > 0:
    a.append(digits[n % p])
    n //= p
print(*a[::-1], sep='')

