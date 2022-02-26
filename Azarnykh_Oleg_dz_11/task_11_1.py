import re


class Date:
    """Класс, принимающий дату в виде строки формата день-месяц-год"""

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_number(cls, date: str):
        """Извлекает число, месяц, год и преобразовывает их тип к типу «Число»"""
        RE_SPLIT = re.compile(r'[./-]')
        day, month, year = int(RE_SPLIT.split(date)[0]), int(RE_SPLIT.split(date)[1]), int(RE_SPLIT.split(date)[2])
        return f'day = {day}, month = {month}, year = {year}'

    @staticmethod
    def validation(date: str):
        """Проводит валидацию числа, месяца и года"""
        try:
            RE_SPLIT = re.compile(r'[./-]')
            day, month, year = int(RE_SPLIT.split(date)[0]), int(RE_SPLIT.split(date)[1]), int(RE_SPLIT.split(date)[2])
        except ValueError:
            return f'Введено не числовое значение: {date}'
        else:
            valid = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                valid = valid
            else:
                valid[2] = 28
            if 0 <= year // 1000 <= 2 and 1 <= month <= 12 and valid[month] >= day:
                return f'Допустимое значение: {date}'
            else:
                return f'Недопустимая дата: {date}'


if __name__ == '__main__':
    print(Date.date_number('01.12.1234'))
    print(Date.validation('29.02.16'))
    print(Date.validation('29/02/2024'))
    print(Date.validation('29-02-2024'))
    print(Date.validation('29.02.2024'))
    print(Date.validation('29.02.2001'))
    print(Date.validation('01.23.2022'))
    print(Date.validation('32.08.1898'))
    print(Date.validation('01.rr.2021'))

"""
day = 1, month = 12, year = 1234
Допустимое значение: 29.02.16
Допустимое значение: 29/02/2024
Допустимое значение: 29-02-2024
Допустимое значение: 29.02.2024
Недопустимая дата: 29.02.2001
Недопустимая дата: 01.23.2022
Недопустимая дата: 32.08.1898
Введено не числовое значение: 01.rr.2021
"""
