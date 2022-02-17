import time
import sys


class TrafficLight:
    __color: str = "red"

    def running(self):
        mode = {'red': 4, 'yellow': 2, 'green': 3}
        for key, value in mode.items():
            TrafficLight.__color = key
            for t in range(0, value + 1):
                sys.stdout.write("\r")
                sys.stdout.write(f'{TrafficLight.__color} {t} сек')
                time.sleep(1)
            sys.stdout.write("\n")


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
