from random import *

answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
    'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
    'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять',
    'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно'
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Давай познакомимся! ')
name = input('Напиши своё имя: ').capitalize()
print(f'Привет {name}')
print()

while True:
    question = input(f'{name}, задай свой вопрос: ')
    print()
    print("Ответ на вопрос: ")
    print(f'{name}, {choice(answers)}')
    print()
    print('Хотите задать новый вопрос?', 'Если да, нажмите enter или введите любой символ',
          'Если желаете закончить с вопросами введите "НЕТ"', sep='\n')
    ending = input()
    if ending.lower() in ['ytn', 'нет', 'не', 'тщ', 'no', 'n', 'т', 'y', 'н']:
        print(f'{name}, возвращайся, если возникнут вопросы!')
        break
    print(f'Отлично, {ending} это еще не конец, продолжаем >(^-^)<')
    print()
