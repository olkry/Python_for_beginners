number = int(input())
count_tree = 0
last_digit = number % 10
last_count = 0
chet_num_count = 0
summ_over_five = 0
proiz_over_seven = 1
count_zero_five = 0
while number > 0:
    digit = number % 10
    if digit == 3:
        count_tree += 1
    if digit == last_digit:
        last_count += 1
    if digit % 2 == 0:
        chet_num_count += 1
    if digit > 5:
        summ_over_five += digit
    if digit > 7:
        proiz_over_seven *= digit
    if digit == 0 or digit == 5:
        count_zero_five += 1
    number //= 10

print(count_tree, last_count, chet_num_count, summ_over_five, proiz_over_seven, count_zero_five, sep='\n')
