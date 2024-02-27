# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2 и
# возвращает значение True, если слова имеют одинаковую длину и отличаются ровно в одном символе и False  в противном случае.

# объявление функции
def is_one_away(word1, word2):
    err_count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                err_count += 1
        return err_count == 1
    else:
        return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
