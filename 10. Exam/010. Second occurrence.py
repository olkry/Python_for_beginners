word = input()
count = word.count('f')

if count >= 2:
    triger = 0
    for i in range(len(word)):
        if word[i] == 'f' and triger < 2:
            triger += 1
            number = i
    print(number)
else:
    print(-1 if count == 1 else -2)

print('-----------------')

s = input()

if s.count("f") == 0:
    print(-2)
elif s.count("f") == 1:
    print(-1)
else:
    res = s.replace("f", ".", 1).find("f")
    print(res)
