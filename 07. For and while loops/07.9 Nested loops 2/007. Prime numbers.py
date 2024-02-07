# На вход программе подается два натуральных числа a и b (a< b).
# Напишите программу, которая находит все простые числа от a до b включительно.

# num_a = int(input())
# num_b = int(input())
# for i in range(num_a, num_b+1):
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count +=1
#     if count == 2:
#         print(j)
#
# print('__________________________')
#
# a, b = int(input()), int(input())
#
# for cur_num in range(a, b + 1):
#     if cur_num == 1:
#         continue
#
#     for i in range(2, int(cur_num ** 0.5 + 1)):
#         if cur_num % i == 0:
#             break
#     else:
#         print(cur_num)
# print('__________________________')

a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)