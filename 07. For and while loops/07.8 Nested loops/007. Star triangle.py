# Дано нечетное натуральное число n. Напишите программу, которая печатает равнобедренный
# звездный треугольник с основанием, равным n в соответствии с примером(7):
# *
# **
# ***
# ****
# ***
# **
# *

n = int(input())
count = 1

for i in range(n):
    print("*" * count)
    if i < n // 2:
        count += 1
    else:
        count -= 1


# Any

# n = int(input())
#
# for i in range(n):
#     cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
#     for j in range(cur_cnt):
#         print("*", end="")
#     print()

# Any

# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(i):
#         if i + j <= n:
#             print('*', end='')
#
#     print()