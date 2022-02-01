def get_uniq_numbers(src: list):
    """Определяет элементы списка, не имеющие повторений, с сохранением исходного порядка ("в лоб")"""
    screening_set = set()
    uniq_list = []
    for num in src:
        if num not in screening_set:
            uniq_list.append(num)
            screening_set.add(num)
        elif num in uniq_list:
            uniq_list.remove(num)
    return uniq_list


def get_uniq_numbers_adv(src: list):
    """Определяет элементы списка, не имеющие повторений, с сохранением исходного порядка"""
    return [num for num in src if src.count(num) == 1]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(get_uniq_numbers(src))
print(get_uniq_numbers_adv(src))
