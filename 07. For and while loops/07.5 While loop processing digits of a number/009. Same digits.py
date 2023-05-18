# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input())
control = 'YES'

while num > 9:
    last_dig = num % 10
    pre_last = (num // 10) % 10
    if pre_last != last_dig:
        control = 'NO'
    num //= 10
print(control)

# OR

n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer)    
