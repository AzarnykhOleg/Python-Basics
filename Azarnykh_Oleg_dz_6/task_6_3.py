import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    users_list = []
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        for str_ in fr:
            users_list.append(str_.replace(',', ' '))

    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        for str_ in fr:
            hobby_list.append(str_)

    users_dict = {}
    if len(users_list) >= len(hobby_list):
        while len(users_list) > len(hobby_list):
            hobby_list.append(None)
        counter = 0
        for name in users_list:
            users_dict[name] = hobby_list[counter]
            counter += 1
    else:
        users_dict = sys.exit(1)

    return users_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
