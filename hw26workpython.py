import os
import random
from gtts import gTTS
import playsound
import speech_recognition as sr

film = ['терминатор', 'терминатор2', 'рембо', 'Элемент']
hello = ['Здарова корова', 'здоровее видали', 'Привет', 'отстань']

def listen():
    print('Скажи команду')
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        voice1 = rec.listen(source, phrase_time_limit=5)

        try:
            com = rec.recognize_google(voice1, language='ru')
            print('Вы сказали:', com)
            vibor(com)

        except:
            print('Не могу понять')

def vibor(msg):
    msg = msg.lower()
    if 'привет' in msg:
        h = random.choice(hello)
        action(h)
    elif 'как дела' in msg:
        action('Пойдет!')
    elif 'какой фильм посмотреть' in msg:
        r = random.choice(film)
        action(r)
    elif 'расскажи анекдот' in msg:
        action('сам себя смеши жопа')
    elif 'пока' in msg:
        action('до свидания')
        os.abort()
    elif 'посчитай' in msg:
        action('Хорошо, давай посчитаем!')
        num1 = get_number('Скажи первое число: ')
        operation = get_operation()
        num2 = get_number('Скажи второе число: ')

        calc(num1, num2, operation)
    else:
        action(msg)

def get_number(prompt):
    print(prompt)
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        voice = rec.listen(source, phrase_time_limit=5)
        try:
            number = int(rec.recognize_google(voice, language='ru'))
            print('Вы сказали:', number)
            return number
        except:
            print('Не могу распознать число.')
            return 0

def get_operation():
    print('Скажи, что сделать с числами? (плюс, минус, умножить, разделить)')
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        voice = rec.listen(source, phrase_time_limit=5)
        try:
            operation = rec.recognize_google(voice, language='ru')
            print('Вы сказали:', operation)
            return operation
        except:
            print('Не могу распознать операцию.')
            return ''

def calc(num1, num2, operation):
    if operation == 'плюс':
        result = num1 + num2
        print(f"Сумма чисел равна {result}")
        action(f"Сумма чисел равна {result}")
    elif operation == 'минус':
        result = num1 - num2
        print(f"Разность чисел равна {result}")
        action(f"Разность чисел равна {result}")
    elif operation == 'умножить':
        result = num1 * num2
        print(f"Произведение чисел равно {result}")
        action(f"Произведение чисел равно {result}")
    elif operation == 'разделить':
        if num2 != 0:
            result = num1 / num2
            print(f"Частное чисел равно {result}")
            action(f"Частное чисел равно {result}")
        else:
            print("Ошибка! Нельзя делить на ноль.")
            action("Ошибка! Нельзя делить на ноль.")

def action(say):
    print('Бот:', say)
    voice = gTTS(say, lang='ru')
    fname = 'output.mp3'
    voice.save(fname)
    playsound.playsound(fname)
    os.remove(fname)

while True:
    listen()
