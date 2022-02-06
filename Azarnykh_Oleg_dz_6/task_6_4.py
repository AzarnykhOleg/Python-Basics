import sys


def prepare_dataset(path_users_file: str, path_hobby_file: str):
    with open(path_users_file, 'r', encoding='utf-8') as fr_1, open(path_hobby_file, 'r',
        encoding='utf-8') as fr_2, open('task_6_4_result.json', 'w+', encoding='utf-8') as fw:
        len_fr_1 = sum(1 for str_ in fr_1)
        len_fr_2 = sum(1 for str_ in fr_2)
        fr_1.seek(0)
        fr_2.seek(0)

        if len_fr_1 >= len_fr_2:
            count = 0
            for str_1 in fr_1:
                str_1 = str_1.replace(',', ' ').strip()
                str_2 = fr_2.readline() if count < len_fr_2 else None
                count += 1
                fw.write(f'{str_1}: {str_2}')
        else:
            sys.exit(1)


prepare_dataset('users.csv', 'hobby.csv')
