word = input()
new_str = ''
for i in range(len(word)):
    if i % 3 != 0:
        new_str += word[i]

print(new_str)
