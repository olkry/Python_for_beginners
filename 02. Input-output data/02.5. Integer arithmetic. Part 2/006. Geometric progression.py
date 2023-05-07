# A geometric progression is a sequence of numbers b1,b2,b3...bn, each of which,
# starting from b2, is obtained from the previous one by multiplying by the same
# constant number q(the denominator of the progression), bn = bn-1 * q.
# If the first term of the progression and its denominator are known, then
# The n-th member of the geometric progression is found by the formula bn = b1*qn-1
#
# Геометрической прогрессией называется последовательность чисел b1,b2,b3...bn,
# каждое из которых, начиная с b2, получается из предыдущего умножением на одно и то же
# постоянное число q(знаменатель прогрессии), bn = bn-1 * q.
# Если известен первый член прогрессии и её знаменатель, то
# n-ый член геометрической прогрессии находится по формуле bn = b1*qn-1

b1 = int(input())
q = int(input())
n = int(input())
print(b1 * q ** (n - 1))
