chunk_size = 256
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    str_data = []
    while True:
        chunk = fr.read(chunk_size)
        if not chunk:
            break

        spammer = {}
        for str_ in fr:
            if str_.split()[0] not in spammer:
                spammer[str_.split()[0]] = 1
            else:
                spammer[str_.split()[0]] += 1

for key, val in spammer.items():
    if val == max(spammer.values()):
        print(f'Пользователь {key} отправил {val} запросов')
