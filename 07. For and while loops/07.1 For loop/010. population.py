# The input to the program is three natural numbers m, p, n.
# m - starting number of organisms
# p - average daily increase in %
# n - number of days for breeding
# Write a program that predicts the size of a population of organisms.
# The program should output the population size on each day, starting on day 1 and ending on the nth day.
#
# На вход программе подается три натуральных числа m, p, n.
# m - стартовое количество организмов
# p - среднесуточное увеличение в %
# n - количество дней для размножения
# Напишите программу, которая предсказывает размер популяции организмов.
# Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.

m, p, n = int(input()), int(input()), int(input())
for i in range(n):
    print(i + 1, m)
    m += m * (p / 100)
