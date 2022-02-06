import sys


with open('bakery.csv', 'r+', encoding='utf-8') as fw:
    str_counter = 0
    for str in fw.readlines():
        str_counter += 1

with open('bakery.csv', 'r+', encoding='utf-8') as fw:
    if int(sys.argv[1]) > str_counter:
        print(f'Записи № {sys.argv[1]} не существует')
    else:
        counter = 0
        while counter < int(sys.argv[1]):
            str_ = fw.tell()
            line = fw.readline()
            counter += 1
        fw.seek(str_)
        fw.writelines(' '*20)
        fw.seek(str_)
        fw.writelines(sys.argv[2])
