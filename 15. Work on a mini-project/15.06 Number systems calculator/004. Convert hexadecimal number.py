# Переведите шестнадцатеричное число 1AF2 в десятичную систему счисления.


number_inp = '1AF2'
greder = len(number_inp) - 1
num = 0

for number in number_inp:
    if number.isdigit():
        num += int(number) * (16 ** greder)
    else:
        if number == 'A':
            num += 10 * (16 ** greder)
        elif number == 'B':
            num += 11 * (16 ** greder)
        elif number == 'C':
            num += 12 * (16 ** greder)
        elif number == 'D':
            num += 13 * (16 ** greder)
        elif number == 'E':
            num += 14 * (16 ** greder)
        elif number == 'F':
            num += 15 * (16 ** greder)
    greder -= 1

print(num)