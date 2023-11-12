class Rational:
    def __init__(self, __numerator, __denominator):
        self.__numerator = __numerator
        self.__denominator = __denominator
        self.__normalise()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational'):
        new_numerator = self.__numerator * other.numerator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other: 'Rational'):
        new_numerator = self.__numerator * other.denominator
        new_denominator = self.__denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __add__(self, other: 'Rational'):
        new_numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other: 'Rational'):
        new_numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
        new_denominator = self.__denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other: 'Rational'):
        return self.__numerator == other.numerator and self.__denominator == other.denominator

    def __ne__(self, other: 'Rational'):
        return not (self == other)

    def __gt__(self, other: 'Rational'):
        return self.__numerator * other.denominator > other.numerator * self.__denominator

    def __lt__(self, other: 'Rational'):
        return self.__numerator * other.denominator < other.numerator * self.__denominator

    def __ge__(self, other: 'Rational'):
        return self.__numerator * other.denominator >= other.numerator * self.__denominator

    def __le__(self, other: 'Rational'):
        return self.__numerator * other.denominator <= other.numerator * self.__denominator


    def __normalise(self):
        nod: int = Rational.nod(self.__numerator, self.__denominator)
        self.__numerator //= nod
        self.__denominator //= nod

        if self.__denominator < 0:
            self.__numerator = self.__numerator * -1,
            self.__denominator = self.__denominator * -1


    @staticmethod
    def nod(x: int, y: int):
        if x < y:
            x, y = y, x
        while y != 0:
            x, y = y, x % y
        return x


if __name__ == '__main__':
    first = Rational(2, 5)
    second = Rational(4, 6)

    assert str(first) == '2 / 5'
    assert first + second == Rational(16, 15)
    assert first - second == Rational(-4, 15)
    assert first / second == Rational(3, 5)
    assert first * second == Rational(4, 15)

    a = Rational(1, 4)
    b = Rational(3, 2)
    c = Rational(1, 8)
    d = Rational(156, 100)
    assert a * (b + c) + d == Rational(1573, 800)
