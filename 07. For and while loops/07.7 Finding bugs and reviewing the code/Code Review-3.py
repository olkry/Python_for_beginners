# На обработку поступает последовательность из 7 целых чисел. Нужно написать программу, которая подсчитывает и
# выводит сумму всех чётных чисел последовательности или 0, если чётных чисел в последовательности нет.
# Программист торопился и написал программу неправильно.
#
# Найдите все ошибки в этой программе (их ровно 4). Известно, что каждая ошибка затрагивает только одну строку и
# может быть исправлена без изменения других строк.

s = 0
for _ in range(7):
    n = int(input())
    if n % 2 == 0:
        s += n
print(s)
