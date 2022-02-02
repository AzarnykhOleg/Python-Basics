def get_numbers(src: list):
    yield [num for num in src if num > src[src.index(num) - 1]]


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 444]
print(*get_numbers(src))
print(type(get_numbers(src)))
