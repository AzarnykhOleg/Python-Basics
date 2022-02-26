class ComplexNumber:
    def __init__(self, re: float, im: float):
        self.re = re
        self.im = im

    def __add__(self, other):
        re = self.re + other.re
        im = self.im + other.im
        return f'({self.re} + {self.im}i) + ({other.re} + {other.im}i) = {re} + {im}i'

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return f'({self.re} + {self.im}i) * ({other.re} + {other.im}i) = {re} + {im}i'


if __name__ == '__main__':
    a = ComplexNumber(5, 8)
    b = ComplexNumber(2, -3)
    c = ComplexNumber(3, -2)
    d = ComplexNumber(-3, 4)
    print(a + b)
    print(a + c)
    print(c + d)
    print(a * b)
    print(a * c)
    print(c * d)
