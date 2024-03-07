# В саду 88n фруктовых деревьев, из них 32n яблони, 22n груши, 16n слив и 17n вишен. В какой системе счисления посчитаны деревья?
# Примечание. Переведите числа из n-ой системы счисления в десятичную и составьте уравнение.
#
# 32 = 3 * x ** 1 + 2 * x ** 0 = 3x+2
# 22 = 3 * x ** 1 + 2 * x ** 0 = 2x+2
# 16 = 1 * x ** 1 + 6 * x ** 0 = x+6
# 17 = 1 * x ** 1 + 7 * x ** 0 = x+7
# 88 = 8 * x **1 + 8 * x ** 0 = 8x+8
#
# Теперь пишем уравнение:
# 32+22+16+17=88
#
# Производим замену:
# (3х+2)  + (2х+2) + (х+6) + (х+7) = 8х+8
# Находим Х. Это и есть основание.

for x in range(10):
    if (3*x+2) + (2*x+2)+(x+6)+(x+7) == 8*x+8:
        print(x)