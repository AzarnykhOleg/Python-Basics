import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_folder = os.path.join(BASE_DIR, 'my_project')
new_folder = os.path.join(base_folder, 'templates')

try:
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
except FileNotFoundError as err:
    print(f'Директория для сбора шаблонов указана не верно или скрипт запущен вне этой директории: {err}')

for dirpsth, dirnames, filenames in os.walk(base_folder):
    for el in filenames:
        if el.split('.')[-1] == 'html':
            dir_folder = os.path.join(new_folder, dirpsth.split('\\')[-1])
            if not os.path.exists(dir_folder):
                os.mkdir(dir_folder)
            file_folder = os.path.join(dirpsth, el)
            new_file_folder = os.path.join(dir_folder, el)
            if not os.path.exists(new_file_folder):
                shutil.copy(file_folder, new_file_folder)
