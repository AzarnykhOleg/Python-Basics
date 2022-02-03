def convert_list_in_str(list_in: list) -> str:
    for some_str in list_in:
        if some_str.isdigit():
            some_str_1 = int(some_str)
            list_in[list_in.index(some_str)] = f'"{some_str_1:02d}"'
        elif some_str[0] == '+':
            some_str_1 = int(some_str[1:])
            list_in[list_in.index(some_str)] = f'"+{some_str_1:02d}"'
        elif some_str[0] == '-':
            some_str_1 = int(some_str[1:])
            list_in[list_in.index(some_str)] = f'"-{some_str_1:02d}"'
    str_out = ' '.join(list_in)
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

    # Проверка на "in place"
'''for some_str in my_list:
    print(my_list, id(my_list))
    if some_str.isdigit():
        some_str_1 = int(some_str)
        my_list[my_list.index(some_str)] = f'"{some_str_1:02d}"'
    elif some_str[0] == '+':
        some_str_1 = int(some_str[1:])
        my_list[my_list.index(some_str)] = f'"+{some_str_1:02d}"'
    elif some_str[0] == '-':
        some_str_1 = int(some_str[1:])
        my_list[my_list.index(some_str)] = f'"-{some_str_1:02d}"'

print(' '.join(my_list))'''
