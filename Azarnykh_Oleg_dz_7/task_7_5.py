import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def w_t_file (file_name, dict_tuple):
    dict_tuple = list(dict_tuple)
    dict_tuple[0] += 1
    file_name = file_name.split('.')[-1]
    if not file_name in dict_tuple[1]:
        dict_tuple[1].append(file_name)
    dict_tuple = tuple(dict_tuple)
    return dict_tuple


def statistics(some_dir):
    base_folder = os.path.join(BASE_DIR, some_dir)
    file_dict = {0: (0, []), 10: (0, []), 100: (0, []), 1000: (0, []), 10000: (0, []), 100000: (0, []), "> 100000": (0, [])}
    for dirpsth, dirnames, filenames in os.walk(some_dir):
        for el in filenames:
            el_sise = os.stat(os.path.join(base_folder, el)).st_size
            for i in range(1, 9):
                if 10 ** (i - 1) <= el_sise <= 10 ** i:
                    file_dict[10 ** i] = w_t_file(el, file_dict[10 ** i])
                elif el_sise > 10 ** 6:
                    file_dict["более 100000"] = w_t_file(el, file_dict[10 ** i])
                elif el_sise == 0:
                    val_1_file_dict_0 = w_t_file(el, file_dict[0])
        val_2_file_dict_0 = len(filenames) - sum(val[0] for val in file_dict.values())
        val_1_file_dict_0 = list(val_1_file_dict_0)[1]
        file_dict[0] = val_2_file_dict_0, val_1_file_dict_0

        file_dict_1 = {key: val for key, val in file_dict.items()}
        for key, value in file_dict.items():
            if value[0] == 0:
                del file_dict_1[key]

        with open('task_7_5_result.json', 'w', encoding='utf-8') as fw:
            json.dump(file_dict_1, fw, ensure_ascii=False, indent=2)

    return file_dict_1


if __name__ == "__main__":
    print(statistics('some_data'))
