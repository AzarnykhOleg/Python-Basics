import sys


with open('bakery.csv', 'a+', encoding='utf-8') as fw:
    fw.writelines(sys.argv[1])
    fw.write(' '*30)
    fw.write('\n')
