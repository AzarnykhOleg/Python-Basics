def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский (Update)"""
    e_r_dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if value in e_r_dictionary:
        str_out = e_r_dictionary[value]
    elif value.lower() in e_r_dictionary:
        str_out = e_r_dictionary[value.lower()].capitalize()
    else:
        str_out = None
    return str_out


print(num_translate_adv("One"))
print(num_translate_adv("eight"))
print(num_translate_adv("twelve"))
