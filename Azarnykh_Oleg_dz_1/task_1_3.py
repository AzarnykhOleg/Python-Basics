def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    number = str(number)
    if number != '11' and number[-1] == '1':
        word = ' процент'
    elif number == '12' or number == '13' or number == '14':
        word = ' процентов'
    elif number[-1] == '2' or number[-1] == '3' or number[-1] == '4':
        word = ' процента'
    else:
        word = ' процентов'
    phrase = number + word
    return phrase


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
