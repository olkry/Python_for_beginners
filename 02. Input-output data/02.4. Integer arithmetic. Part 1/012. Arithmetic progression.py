# An arithmetic progression is a sequence of numbers a1, a2, a3...an,
# each of which, starting from a2, is obtained from the previous one
# by adding to it the same constant number d (the difference of the progression),
# that is: an = an-1+ d.
# If the first member of the progression and its difference are known,
# then the n-th member of the arithmetic progression is found by the formula: an = a1+d(n-1)
#
# Арифметической прогрессией называется последовательность чисел a1, a2, a3...an,
# каждое из которых, начиная с a2, получается из предыдущего прибавлением к нему одного и
# того же постоянного числа d(разность прогрессии), то есть: an = an-1+d.
# Если известен первый член прогрессии и её разность, то n-ый член арифметической прогрессии находится по формуле:
# an = a1+d(n-1)

a1 = int(input())
d = int(input())
n = int(input())
print(a1 + d * (n - 1))
