# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
sqar_sum = 0
for num in numbers:
    sqar_sum += num ** 2
print(sqar_sum)