import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def statistics(some_dir):
    base_folder = os.path.join(BASE_DIR, some_dir)
    file_dict = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, "более 100000": 0}
    for dirpsth, dirnames, filenames in os.walk(some_dir):
        for el in filenames:
            el_sise = os.stat(os.path.join(base_folder, el)).st_size
            for i in range(1, 9):
                if 10 ** (i - 1) < el_sise <= 10 ** i:
                    file_dict[10 ** i] += 1
                elif el_sise > 10 ** 6:
                    file_dict["более 1000000"] += 1
        file_dict[0] = len(filenames) - sum(val for val in file_dict.values())

        file_dict_1 = {key: val for key, val in file_dict.items()}
        for key, value in file_dict.items():
            if value == 0:
                del file_dict_1[key]

    return file_dict_1


if __name__ == "__main__":
    print(statistics('some_data'))
