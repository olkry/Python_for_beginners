# Two segments are given on the number line: [a1; b1] and [a2; b2].
# Write a program that finds their intersection.
# The intersection of two segments can be: segment; dot; empty set.
#
# На числовой прямой даны два отрезка: [a1; b1] и [a2; b2].
# Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть: отрезок; точка; пустое множество.

a, b, c, d = int(input()), int(input()), int(input()), int(input())
if c <= a <= d and c <= b <= d:
    print(a, b)
elif c <= b <= d and a <= c <= b:
    if b == c:
        print(b)
    elif b > c:
        print(c, b)
    else:
        print(b, c)
elif c <= a <= d and a <= c <= b:
    if a == c:
        print(a)
    elif a > c:
        print(c, b)
    else:
        print(a, c)
elif c <= b <= d and a <= d <= b:
    if b == d:
        print(b)
    elif b > d:
        print(c, b)
    else:
        print(b, d)
elif c <= a <= d and a <= d <= b:
    if a == d:
        print(a)
    elif a > d:
        print(d, a)
    else:
        print(a, d)
elif a <= c <= b and a <= d <= b:
    print(c, d)
elif a <= c <= b:
    print(c)
elif a <= d <= b:
    print(d)
elif c <= a <= d:
    print(a)
elif c <= b <= d:
    print(b)
else:
    if (a != c or d) and (b != c or d): print('пустое множество')
