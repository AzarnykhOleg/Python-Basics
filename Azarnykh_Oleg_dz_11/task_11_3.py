class OnlyNumbersList(Exception):
    """Класс-исключение, проверяющий содержимое списка на наличие только чисел"""

    def __init__(self, message: str = 'Введён не числовой элемент'):
        self.message = message

    def __str__(self):
        return self.message


if __name__ == '__main__':
    my_list = []
    while True:
        el = input('Введите элемент списка. Для завершения введите "stop" : ')
        if el == "stop":
            break
        else:
            try:
                if not el.isdigit():
                    raise OnlyNumbersList()
                else:
                    my_list.append(el)
            except OnlyNumbersList as err:
                print(err)
    print(my_list)
