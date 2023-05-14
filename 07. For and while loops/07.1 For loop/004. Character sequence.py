# Write a program that uses exactly three for loops to print the following sequence of characters:
#
# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:
#     AAA
#     AAA
#     AAA
#     AAA
#     AAA
#     AAA
#     BBBB
#     BBBB
#     BBBB
#     BBBB
#     BBBB
#     E
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     TTTTT
#     G

for _ in range(6):
    print('A' * 3)
for _ in range(5):
    print('B' * 4)
print('E')
for _ in range(9):
    print('T' * 5)
print('G')
