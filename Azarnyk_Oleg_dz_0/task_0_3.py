import time
print('Загадайте число от 0 до 100. Я попробую его отгадать.')
time.sleep(2)
print('Дайте мне несколько попыток.')
time.sleep(2)
print('Если загаданное Вами число меньше моего ответа, введите знак "<"')
time.sleep(2)
print('Если загаданное Вами число больше моего ответа, введите знак ">"')
time.sleep(2)
print('Если я угадал загаданное Вами число, введите знак "="')
time.sleep(2)
print('Загадали?')
time.sleep(3)
print('Поехали!')

import random
stop = None
hint = None
numbers = range(0, 101)
numbers = list(numbers)

while hint != '=':
    attempt = random.choice(numbers)
    hint = str(input('Ваше число ' + str(attempt) + '? Подсказка: заганное число '))
    if hint == '=':
        print('Ура! Поздравьте меня с победой!')
        break
    elif hint == '<':
        stop = numbers.index(attempt)
        del numbers[stop:len(numbers)]
    elif hint == '>':
        stop = numbers.index(attempt)
        del numbers[:(stop+1)]


