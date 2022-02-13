import re
from functools import wraps


def val_checker(valid=0):
    def val_check(func):
        @wraps(func)
        def val_chec(*arg, **kwargs):
            RE_VALID = re.compile(r'^[1-9]+[0-9]*')
            for a in arg:
                chec = RE_VALID.match(str(a))
                if valid == 0:
                    return func(*arg, **kwargs)
                else:
                    try:
                        if chec:
                            return func(*arg, **kwargs)
                        else:
                            raise ValueError(f'wrong val {a}')
                    except ValueError as err:
                        print(err)
        return val_chec
    return val_check


@val_checker(valid=1)
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(9))
    print(calc_cube(-9))
    print(calc_cube('ss'))
    print(calc_cube.__name__)
