def sum_list_1(dataset: list) -> int:
    # Вычисляем сумму чисел списка dataset, сумма цифр которых делится нацело на 7
    sum_1 = 0
    for number in dataset:
        counter = 0
        sum_number = 0
        while number % 10 ** counter < number:
            sum_number += number % 10 ** (counter + 1) // 10 ** counter
            counter += 1
        if sum_number % 7 == 0:
            sum_1 += number
    return sum_1


def sum_list_2(dataset: list) -> int:
    # К каждому элементу списка добавляем 17
    dataset_1 = []
    for number in dataset:
        dataset_1.append(number + 17)

    # и вычисляем сумму чисел списка, сумма цифр которых делится нацело на 7
    sum_2 = 0
    for number in dataset_1:
        counter = 0
        sum_number = 0
        while number % 10 ** counter < number:
            sum_number += number % 10 ** (counter + 1) // 10 ** counter
            counter += 1
        if sum_number % 7 == 0:
            sum_2 += number
    return sum_2


def sum_list_3(dataset: list) -> int:
    # К каждому элементу списка добавляем 17 и вычисляем сумму чисел списка,
    # сумма цифр которых делится нацело на 7
    sum_3 = 0
    for number in dataset:
        counter = 0
        sum_number = 0
        while (number + 17) % 10 ** counter < (number + 17):
            sum_number += (number + 17) % 10 ** (counter + 1) // 10 ** counter
            counter += 1
        if sum_number % 7 == 0:
            sum_3 += (number + 17)
    return sum_3

    # Создаём список, состоящий из кубов нечётных чисел от 1 до 1000
my_list = []
for i in range(1, 1000, 2):
    my_list.append(i ** 3)


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)
