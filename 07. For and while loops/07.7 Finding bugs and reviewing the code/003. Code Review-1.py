# На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают
# 10^6. Нужно написать программу, которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
# Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку
# и может быть исправлена без изменения других строк.

count = 0
product_num = 1
for i in range(10):
    num = int(input())
    if num >= 0:
        product_num = product_num * num
        count = count + 1
if count > 0:
    print(count)
    print(product_num)
else:
    print('NO')
