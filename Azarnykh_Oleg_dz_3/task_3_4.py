def thesaurus(*args) -> dict:
    dict_out = {}
    for arg in args:
        if arg.split(' ')[1][0] not in dict_out.keys():
            dict_out[arg.split(' ')[1][0]] = [arg]
        else:
            dict_out[arg.split(' ')[1][0]] = [*dict_out[arg.split(' ')[1][0]], arg]
    dict_out = dict(sorted(dict_out.items()))

    for key in dict_out:
        dict_out_ = {}
        for names in dict_out[key]:                                 # перебор списков имён и фамилий в основном словаре
            if names.split(' ')[0][0] not in dict_out_.keys():      # проверка первой буквы имени в новом словаре
                dict_out_[names.split(' ')[0][0]] = [names]
            else:
                dict_out_[names.split(' ')[0][0]] = [*dict_out_[names.split(' ')[0][0]], names]
        dict_out[key] = dict(sorted(dict_out_.items()))

    return dict_out


print(thesaurus("Иван Петров", "Мария Панина", "Петр Иванов", "Илья Ильин", "Борис Иващенко",
                    "Ирина Пухова", "Михаил Абаносимов", "Игнат Петров", "Игорь Акунин"))
