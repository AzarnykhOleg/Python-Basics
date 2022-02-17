import sys


class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed: int = speed
        self.color: str = color
        self.name: str = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed = self.speed + 15
        sys.stdout.write(f'Машина {self.name} повысила скорость на 15: {self.speed}\n')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        sys.stdout.write(f'{self.name} остановилась\n')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction == 'направо' or direction == 'налево' or direction == 'прямо' or direction == 'назад':
            sys.stdout.write(f'{self.name} движется {direction}\n')
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self.is_police:
            sys.stdout.write(f'{self.name} текущая скорость {self.speed} км/час\n'
                             f'Вруби мигалку и забудь про скорость!\n')
        else:
            sys.stdout.write(f'{self.name} текущая скорость {self.speed} км/час\n')


class TownCar(Car):
    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: при скорости выше 60 км/ч
            в stdout выводит сообщение формата 'Alarm!!! Speed!!!'
        """
        if self.speed > 60:
            sys.stdout.write('Alarm!!! Speed!!!\n')
        else:
            sys.stdout.write(f'{self.name} текущая скорость {self.speed} км/час\n')


class WorkCar(Car):
    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: при скорости выше 40 км/ч
            в stdout выводит сообщение формата 'Alarm!!! Speed!!!'
        """
        if self.speed > 40:
            sys.stdout.write('Alarm!!! Speed!!!\n')
        else:
            sys.stdout.write(f'{self.name} текущая скорость {self.speed} км/час\n')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police: bool = True


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """
