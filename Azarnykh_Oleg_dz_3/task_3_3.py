def thesaurus(*args) -> dict:
    dict_out = {}
    for arg in args:
        if arg[0] not in dict_out.keys():
            dict_out[arg[0]] = [arg]
        else:
            dict_out[arg[0]] = sorted([*dict_out[arg[0]], arg])
    dict_out = dict(sorted(dict_out.items()))
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Борис", "Ирина", "Михаил", "Игнат", "Игорь"))