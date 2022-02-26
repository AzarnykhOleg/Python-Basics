from abc import ABC, abstractmethod


def valid_arg(method):
    """Валидация вводимых данных о количестве передаваемого/принимаемого на склад имущества"""
    def valid(*args):
        if not isinstance(args[1], int):
            print(f'Недопустимое значение: "{args[1]}"')
        else:
            return method(*args)
    return valid


class Warehouse(ABC):
    """Класс, описывающий склад"""
    asset = {}
    title = '"Склад"'

    @classmethod
    def list_of_asset(cls):
        """Выводит список имеющегося на складе имущества"""
        del_set = {}
        for key, val in Warehouse.asset.items():
            for key_, val_ in Warehouse.asset[key].items():
                if val_ == 0:
                    del_set[key] = key_
        for key, val in del_set.items():
            del Warehouse.asset[key][val]
        del_list = []
        for key, val in Warehouse.asset.items():
            if val == {}:
                del_list.append(key)
        for el in del_list:
            del Warehouse.asset[el]
        str_of_asset = '\r'
        for key in Warehouse.asset.keys():
            str_of_asset_ = f'{key}ы:\n'
            for key_, val in Warehouse.asset[key].items():
                str_of_asset_ += f'\t\t\t{key_} - {val} шт.\n'
            str_of_asset += str_of_asset_
        print(f'В {Warehouse.title} в наличии следующее имущество:\n {str_of_asset}')

    @classmethod
    @valid_arg
    def reception(cls, count: int, types: str, model: str):
        """Осуществляет приём имущества на склад
        :param count: количесво единиц видов передаваемого на склад имущества
        :param types: вид передаваемого на склад имущества
        :param model: модель передаваемого на склад имущества
        """
        if types not in Warehouse.asset:
            Warehouse.asset[types] = {model: count}
        else:
            if model not in Warehouse.asset[types]:
                Warehouse.asset[types][model] = count
            else:
                Warehouse.asset[types][model] += count
        print(f'В {Warehouse.title} поступило {count} {types} {model}')

    @classmethod
    @valid_arg
    def transfer(cls, count: int, types: str, model: str, division: str):
        """
        Осуществляет передачу имущества со склада
        :param count: количесво единиц видов передаваемого на склад имущества
        :param types: вид передаваемого на склад имущества
        :param model: модель передаваемого на склад имущества
        :param division: отдел, в который передаётся имущество со склада
        """
        if types not in Warehouse.asset:
            print(f'В настоящее время в {Warehouse.title} нет {types}')
        elif model not in Warehouse.asset[types]:
            print(f'В настоящее время в {Warehouse.title} нет {types} {model}')
        elif Warehouse.asset[types][model] >= count:
            Warehouse.asset[types][model] -= count
            print(f'{count} {types} {model} передано в {division}')
        else:
            print(f'В {Warehouse.title} в наличии только {Warehouse.asset[types][model]} {types} {model}')
            answer = input(f'Передать {Warehouse.asset[types][model]} {types} {model} в {division}? (да/нет): ')
            if answer == 'да':
                count = Warehouse.asset[types][model]
                Warehouse.transfer(count, types, model, division)


class OfficeEquipment(ABC):
    @abstractmethod
    def transfer(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model: str):
        self.types = 'принтер'
        self.model = model
        self.on_warehouse = False

    def __str__(self):
        return f'{self.types} модель "{self.model}"'

    def transfer(self):
        """Передаёт экземпляр класса на склад"""
        if self.on_warehouse:
            print(f'{self.types} {self.model} уже передан в {Warehouse.title}')
        else:
            Warehouse.reception(1, self.types, self.model)
            self.on_warehouse = True


class Scanner(OfficeEquipment):
    def __init__(self, model: str):
        self.types = 'сканер'
        self.model = model
        self.on_warehouse = False

    def __str__(self):
        return f'{self.types} модель "{self.model}"'

    def transfer(self):
        """Передаёт экземпляр класса на склад"""
        if self.on_warehouse:
            print(f'{self.types} {self.model} уже передан в {Warehouse.title}')
        else:
            Warehouse.reception(1, self.types, self.model)
            self.on_warehouse = True


class Copier(OfficeEquipment):
    def __init__(self, model: str):
        self.types = 'ксерокс'
        self.model = model
        self.on_warehouse = False

    def __str__(self):
        return f'{self.types} модель "{self.model}"'

    def transfer(self):
        """Передаёт экземпляр класса на склад"""
        if self.on_warehouse:
            print(f'{self.types} {self.model} уже передан в {Warehouse.title}')
        else:
            Warehouse.reception(1, self.types, self.model)
            self.on_warehouse = True


if __name__ == '__main__':
    printer_1 = Printer('Yota')
    print(printer_1)  # принтер модель "Yota"
    printer_1.transfer()  # В "Склад" поступило 1 принтер Yota
    printer_1.transfer()  # принтер Yota уже передан в "Склад"
    scanner_1 = Scanner('Yota')
    print(scanner_1)  # сканер модель "Yota"
    scanner_1.transfer()  # В "Склад" поступило 1 сканер Yota
    scanner_1.transfer()  # сканер Yota уже передан в "Склад"
    Warehouse.reception(2, 'принтер', 'Canon')  # В "Склад" поступило 2 принтер Canon
    Warehouse.reception(2, 'сканер', 'HP')  # В "Склад" поступило 2 сканер HP
    Warehouse.reception(2, 'сканер', 'LazerJet')  # В "Склад" поступило 2 сканер LazerJet
    Warehouse.reception(4, 'сканер', 'Samsung')  # В "Склад" поступило 4 сканер Samsung
    Warehouse.reception(6, 'сканер', 'Samsung')  # В "Склад" поступило 6 сканер Samsung
    Warehouse.reception(8, 'ксерокс', 'Samsung')  # В "Склад" поступило 8 ксерокс Samsung
    Warehouse.reception(22, 'сканер', 'LazerJet')  # В "Склад" поступило 22 сканер LazerJet
    Warehouse.list_of_asset()
    """
        В "Склад" в наличии следующее имущество:
    принтеры:
                Yota - 1 шт.
                Canon - 2 шт.
    сканеры:
                Yota - 1 шт.
                HP - 2 шт.
                LazerJet - 24 шт.
                Samsung - 10 шт.
    ксероксы:
                Samsung - 8 шт.
    """
    Warehouse.transfer(14, 'сканер', 'LazerJet', 'бухгалтерия')  # 14 сканер LazerJet передано в бухгалтерия
    Warehouse.list_of_asset()
    """
        В "Склад" в наличии следующее имущество:
    принтеры:
                Yota - 1 шт.
                Canon - 2 шт.
    сканеры:
                Yota - 1 шт.
                HP - 2 шт.
                LazerJet - 10 шт.
                Samsung - 10 шт.
    ксероксы:
                Samsung - 8 шт.
    """
    Warehouse.transfer(24, 'монитор', 'Samsung', 'бухгалтерия')  # В настоящее время в "Склад" нет монитор
    Warehouse.transfer(24, 'сканер', 'LG', 'отдел кадров')  # В настоящее время в "Склад" нет сканер LG
    Warehouse.transfer(24, 'сканер', 'LazerJet', 'бухгалтерия')
    """
    В "Склад" в наличии только 10 сканер LazerJet
    Передать 10 сканер LazerJet в бухгалтерия? (да/нет): да
    10 сканер LazerJet передано в бухгалтерия
    """
    Warehouse.list_of_asset()
    """
        В "Склад" в наличии следующее имущество:
    принтеры:
                Yota - 1 шт.
                Canon - 2 шт.
    сканеры:
                Yota - 1 шт.
                HP - 2 шт.
                Samsung - 10 шт.
    ксероксы:
                Samsung - 8 шт.
    """
    Warehouse.transfer(8, 'ксерокс', 'Samsung', 'бухгалтерия')  # 8 ксерокс Samsung передано в бухгалтерия
    Warehouse.list_of_asset()
    """
        В "Склад" в наличии следующее имущество:
    принтеры:
                Yota - 1 шт.
                Canon - 2 шт.
    сканеры:
                Yota - 1 шт.
                HP - 2 шт.
    """
    Warehouse.reception('аа', 'сканер', 'LazerJet')  # Недопустимое значение: "аа"
