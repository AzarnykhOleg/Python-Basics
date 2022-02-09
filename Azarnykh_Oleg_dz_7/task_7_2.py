import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def make_my_dir_adv(base_dir, my_starter):
    for key, val in my_starter.items():
        folder = os.path.join(base_dir, key)
        if not os.path.exists(folder):
            os.mkdir(folder)
        for el in val:
            if isinstance(el, dict):
                make_my_dir_adv(folder, el)
            elif el.split('.') == el:
                folder = os.path.join(base_dir, key, el)
                if not os.path.exists(folder):
                    os.mkdir(folder)
            else:
                f = os.path.join(base_dir, key, el)
                with open(f, 'w', encoding='utf-8'):
                    pass


starter = {'my_project': [{'settings': ['__init__.py', 'dev.py', 'prod.py']},
                          {'mainapp': ['__init__.py', 'models.py', 'views.py',
                                       {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
                          {'authapp': ['__init__.py', 'models.py', 'views.py',
                                      {'templates': [{'authapp': ['base.html', 'index.html']}]}]}]}

if __name__ == "__main__":
    make_my_dir_adv(BASE_DIR, starter)
