number = int(input())
last = 0
while number > 99:
    last = number % 10
    number //= 10
print(last)