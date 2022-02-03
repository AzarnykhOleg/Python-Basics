from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    for element in list_in:
        element_ = str(element)
        ruble, pennies = element_.split('.')
        list_in[list_in.index(element)] = f'{int(ruble)} руб {int(pennies):02d} коп,'
    str_out = ' '.join(list_in)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


print(f'{id(my_list)}: адрес хранения исходного списка.')
result_2 = sort_prices(my_list)
print(f'{id(result_2)}: адрес хранения результата работы функции sort_prices.')
print(result_2)


def sort_price_adv(list_in: list) -> list:
    list_out = list_in.copy()
    list_out.sort(key=None, reverse=True)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    list_out = sort_price_adv(list_in)[0:5]
    return list_out[::-1]


result_4 = check_five_max_elements(my_list)
print(result_4)
