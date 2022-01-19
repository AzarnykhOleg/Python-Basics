def convert_time(duration: int) -> str:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 86400 % 3600 % 60

    if duration >= 86400:
        time_interval = '{} дн {} час {} мин {} сек'.format(days, hours, minutes, seconds)
    elif duration >= 3600:
        time_interval = '{} час {} мин {} сек'.format(hours, minutes, seconds)
    elif duration >= 60:
        time_interval = '{} мин {} сек'.format(minutes, seconds)
    else:
        time_interval = '{} сек'.format(seconds)
    return time_interval

creating_list = int(input('Сколько временных интервалов Вы хотите проверить?\n'))

durations = []
counter = 0
while counter < creating_list:
    duration = int(input('Введите '  + str(counter + 1) +  ' период времени в секундах:\n'))
    durations.append(duration)
    counter += 1

for duration in durations:
    print(convert_time(duration))
