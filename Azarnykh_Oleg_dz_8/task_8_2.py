import re


def pars_my_file(path):
    with open(path, 'r', encoding='utf-8') as fr:
        for str_ in fr:
            try:
                RE_ADDR = re.compile(r'^(\d*\.){3}\d*')
                RE_DATE = re.compile(r'\d{2}/\w{3}/\d{4}:(\d{2}:){2}\d{2}..\d{4}')
                RE_TYPE = re.compile(r'([A-Z]{3,10})')
                RE_RESO = re.compile(r'/[a-z]*/\w*')
                RE_CODE = re.compile(r'\d{3}(?= \d)')
                RE_SIZE = re.compile(r'(?<=\d{3} )\d{1,10}')
                parsed_raw = (RE_ADDR.search(str_).group(), RE_DATE.search(str_).group(), RE_TYPE.search(str_).group(),
                              RE_RESO.search(str_).group(), RE_CODE.search(str_).group(), RE_SIZE.search(str_).group())
                print(parsed_raw)
            except AttributeError as err:
                print(f'Обратить внимание: {str_}: {err}')
                continue


if __name__ == "__main__":
    pars_my_file('nginx_logs.txt')
