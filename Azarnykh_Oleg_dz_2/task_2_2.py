def convert_list_in_str(list_in: list) -> str:
    new_list = []
    for some_str in list_in:
        if some_str.isdigit():
            some_str = int(some_str)
            new_list.append(f'"{some_str:02d}"')
        elif some_str[0] == '+':
            some_str = int(some_str[1:])
            new_list.append(f'"+{some_str:02d}"')
        elif some_str[0] == '-':
            some_str = int(some_str[1:])
            new_list.append(f'"-{some_str:02d}"')
        else:
            new_list.append(some_str)
    str_out = ' '.join(new_list)
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
