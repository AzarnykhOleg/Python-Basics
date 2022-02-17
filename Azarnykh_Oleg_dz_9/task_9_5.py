import sys


class Stationery:

    def __init__(self, title: str) -> None:
        self.title: str = title

    def draw(self) -> None:
        sys.stdout.write('Запуск отрисовки\n')


class Pen(Stationery):
    def draw(self) -> None:
        sys.stdout.write(f'{__class__.__name__}: приступил к отрисовке объекта {self.title}\n')


class Pencil(Stationery):
    def draw(self) -> None:
        Stationery.draw(self)
        sys.stdout.write(f'{__class__.__name__}: приступил к отрисовке объекта {self.title}\n')


class Handle(Stationery):
    def draw(self) -> None:
        sys.stdout.write(f'{__class__.__name__}: приступил к отрисовке объекта {self.title}\n')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
