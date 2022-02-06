from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    yield line.split()[0], line.split()[5][1:], line.split()[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_ in fr:
        list_out.append(*get_parse_attrs(str_))

pprint(list_out)
