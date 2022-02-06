import sys
from itertools import islice

with open('bakery.csv', 'r', encoding='utf-8') as fw:
    if len(sys.argv) == 1:
        print(fw.read())
    elif len(sys.argv) == 2:
        line = fw.readlines()[(int(sys.argv[1]) - 1):]
        for ln in line:
            print(ln.strip())
    elif len(sys.argv) == 3:
        print(*islice(fw.readlines(), int(sys.argv[1]) - 1, int(sys.argv[2])))
    else:
        print('Ошибка ввода данных')
