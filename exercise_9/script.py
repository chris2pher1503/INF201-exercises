""" missing testing """


class Complex:
    def __init__(self, re: float = 0.0, im: float = 0.0):
        self.re = re
        self.im = im

    def __str__(self):
        return f"{self.re}+{self.im}i"

    # addition
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re + other, self.im)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    # multiplication
    def __mul__(self, other):
        if isinstance(other, Complex):
            re = self.re * other.re - self.im * other.im
            im = self.re * other.im + self.im * other.re
            return Complex(re, im)
        elif isinstance(other, (int, float)):
            return Complex(self.re * other, self.im * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # subtraction
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        elif isinstance(other, (int, float)):
            return Complex(self.re - other, self.im)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Complex(other - self.re, -self.im)
        else:
            return NotImplemented

    # Equality
    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


def conjugate(z):
    return Complex(z.re, -z.im)


z = Complex(1, 2)
y = Complex(3, 4)

print(z)

print(z.re)
print(z.im)

print(Complex())
print(Complex(5))

print(z + y)
print(z - y)

print(z + 3)
print(3 + z)
print(z * 3)
print(3 * z)

print(z == y)
print(z != y)

print(conjugate(z))
