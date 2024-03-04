def zero_one_check(char):
    while True:
        if char == '1' or char == '0':
            char = int(char)
            return char
        else:
            print('Некорректные данные! Доступны 1 или 0.')
            char = input()


def shift_check(num, lang):
    while True:
        while num.isdigit():
            if int(num) <= 32 and lang == 1:
                return int(num)
            elif int(num) <= 26 and lang == 0:
                return int(num)
            else:
                print('Некорректные данные. Условия выше')
                num = input()
        else:
            print('Некорректные данные. Условия выше')
            num = input()


def crypter(lang: int, shift: int, text: str):
    message = ''
    while lang:
        for char in text:
            if char.isalpha():
                encode = ord(char) + shift
                if char == char.lower():

                    if encode > ord("я"):
                        message += f'{chr(encode - (ord('я') - ord('а')))}'
                    else:
                        message += f'{chr(encode)}'
                else:

                    if encode > ord("Я"):
                        message += f'{chr(encode - (ord('Я') - ord('А')))}'
                    else:
                        message += f'{chr(encode)}'
            else:
                message += f'{char}'
        return message
    else:
        for char in text:
            if char.isalpha():
                encode = ord(char) + shift
                if char == char.lower():

                    if encode > ord("z"):
                        message += f'{chr(encode - (ord('z') - ord('a')))}'
                    else:
                        message += f'{chr(encode)}'
                else:

                    if encode > ord("Z"):
                        message += f'{chr(encode - (ord('Z') - ord('A')))}'
                    else:
                        message += f'{chr(encode)}'
            else:
                message += f'{char}'
        return message


def uncrypter(lang: int, shift: int, text: str):
    message = ''
    while lang:
        for char in text:
            if char.isalpha():
                encode = ord(char) - shift
                if char == char.lower():

                    if encode < ord("а"):
                        message += f'{chr(encode + (ord('я') - ord('а')))}'
                    else:
                        message += f'{chr(encode)}'
                else:

                    if encode < ord("А"):
                        message += f'{chr(encode + (ord('Я') - ord('А')))}'
                    else:
                        message += f'{chr(encode)}'
            else:
                message += f'{char}'
        return message
    else:
        for char in text:
            if char.isalpha():
                encode = ord(char) - shift
                if char == char.lower():

                    if encode < ord("a"):
                        message += f'{chr(encode + (ord('z') - ord('a')))}'
                    else:
                        message += f'{chr(encode)}'
                else:

                    if encode < ord("A"):
                        message += f'{chr(encode + (ord('Z') - ord('A')))}'
                    else:
                        message += f'{chr(encode)}'
            else:
                message += f'{char}'
        return message


def caesar_crypt(cryp: int, shift: int, lang: int, text: str):
    while cryp:
        return crypter(lang, shift, text)
    else:
        return uncrypter(lang, shift, text)


def text_check(text: str, lang: int):
    while lang:
        while True:
            for char in text:
                if char.isalpha():
                    char = char.lower()
                    if ord('а') <= ord(char) <= ord('я'):
                        continue
                    else:
                        print('Есть символы не русского языка. Введите текст заново')
                        text = input()
                else:
                    continue
            return text
    else:
        while True:
            for char in text:
                if char.isalpha():
                    char = char.lower()
                    if ord('a') <= ord(char) <= ord('z'):
                        continue
                    else:
                        print('Есть символы не английского языка. Введите текст заново')
                        text = input()
                else:
                    continue
            return text


print('Будем шифровать - 1 или дешифровать - 0')
crypt_on = zero_one_check(input())

print('Какой язык используем: 1 - русский, 0 - английский')
language = zero_one_check(input())

print('Для русского алфавита доступно смещение на 32 символа, для английского на 26')
print('Задайте смещение алфавита')
shift = shift_check(input(), language)

print('Введите данные для шифровки на выбранном языке, доступны любые символы:')
input_text = text_check(input(), language)






