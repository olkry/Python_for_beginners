# Дано натуральное число n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.

num = int(input())
max_num = 0
min_num = 10

while num != 0:
    last_dig = num % 10
    if max_num < last_dig:
        max_num = last_dig
    if min_num > last_dig:
        min_num = last_dig
    num //= 10
print(f'Максимальная цифра равна {max_num}', f'Минимальная цифра равна {min_num}', sep='\n')
