# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
sum_dig, dig_num, prod, first_dig, last_num = 0, 0, 1, 0, num % 10

while num != 0:
    last_dig = num % 10
    sum_dig += last_dig
    dig_num += 1
    prod *= last_dig
    if num < 10:
        first_dig = num

    num //= 10
sr_arm = sum_dig / dig_num
summ_fir_las = first_dig + last_num

print(sum_dig, dig_num, prod, sr_arm, first_dig, summ_fir_las, sep='\n')
