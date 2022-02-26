class DivisionByZero(Exception):
    """Класс-исключение, обрабатывающий ситуацию деления на ноль"""

    def __init__(self, message: str = 'Деление на ноль недопустимо'):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    try:
        if divider == 0:
            raise DivisionByZero()
        quotient = round(dividend / divider, 3)
        print(f'Результат деления: {quotient}')
    except DivisionByZero as err:
        print(err)
