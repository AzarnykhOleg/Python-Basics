import random

hidden_number = random.randint(1, 100)
#print(hidden_number)

number_of_players = int(input('Введите количество игроков: '))
gamers = []
i = 0
while i < number_of_players:
    gamer = input('Введите имя игрока № ' + str(i+1) + ': ')
    gamers.append(gamer)
    i = i+1

level = {1: 3, 2: 6, 3: 10}
difficulty_level = int(input('На каком из трёх уровней сложности Вы хотите испытать удачу?: '))
attempt_counter = level[difficulty_level]
counter = 0

answer = None

while counter <= attempt_counter:
    counter = counter + 1
    if counter > attempt_counter:
        print('Поражение. Попытки истрачены.')
    elif answer == hidden_number:
        break
    else:
        for gamer in gamers:
            answer = int(input('Отгадайте число от 1 до 100. Попытка игрока ' + gamer + ': '))
            if answer == hidden_number:
                print('Поздравляем с победой игрока ' + gamer)
                break
            elif answer < hidden_number:
                print('Загадано большее число.')
            else:
                print('Загадано меньшее число.')



