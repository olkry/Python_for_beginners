# Given a positive real number. Print its first digit after the decimal point.
#
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

print(int(float(input()) * 10 % 10))
