def convert_name_extract(list_in: list) -> list:
    list_in_new = []
    for some_str in list_in:
        some_str = some_str.title().split()
        list_in_new.append(f'Привет, {some_str[-1]}!')
    return list_in_new

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
