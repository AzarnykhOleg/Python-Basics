from datetime import datetime
from functools import wraps


def type_logger(func):
    @wraps(func)
    def logging(*arg, **kwargs):
        log_list = []
        for a in arg:
            log_list.append(f'{a}: {type(a)}')
        for key, valye in kwargs.items():
            log_list.append(f'{key} = {valye}')
        log_list = str(f'{log_list[0]}, {log_list[1]}, {log_list[2]}')
        with open('log.txt', 'a+', encoding='utf-8') as log:
            log.write(f'{func.__name__} call_at {datetime.now()} with_arg {log_list}\n')
        return func(*arg, **kwargs)

    return logging


@type_logger
def calc(x, y, **kwargs):
    action = kwargs.get('action', 'add')
    if action == 'add':
        return x + y
    elif action == 'sub':
        return x - y
    elif action == 'mult':
        return x * y
    elif action == 'div':
        return x / y
    elif action == 'exp':
        return x ** y


print(calc(3, 6, action='add'))
print(calc(3, 6, action='sub'))
print(calc(3, 6, action='mult'))
print(calc(3, 6, action='div'))
print(calc(3, 6, action='exp'))

"""
calc call_at 2022-02-12 21:36:50.540439 with_arg 3: <class 'int'>, 6: <class 'int'>, action = add
calc call_at 2022-02-12 21:36:50.540439 with_arg 3: <class 'int'>, 6: <class 'int'>, action = sub
calc call_at 2022-02-12 21:36:50.541439 with_arg 3: <class 'int'>, 6: <class 'int'>, action = mult
calc call_at 2022-02-12 21:36:50.541439 with_arg 3: <class 'int'>, 6: <class 'int'>, action = div
calc call_at 2022-02-12 21:36:50.541439 with_arg 3: <class 'int'>, 6: <class 'int'>, action = exp
"""
