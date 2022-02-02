def check_gen(tutors: list, klasses: list):
    """генератор, возвращающий кортежи вида( < tutor >, < klass >)"""
    for i in range(len(tutors)):
        yield tutors[i], klasses[i] if i < len(klasses) else None


tutors = ['Иван', 'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Данил', 'Михаил']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

generator = check_gen(tutors, klasses)
# print(type(generator), *generator)
# print(next(generator), next(generator), next(generator), sep=', ')
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
