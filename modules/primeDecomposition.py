from functools import reduce
from operator import mul

import modules.primes

primes = modules.primes.Primes()

class PrimeDecomposition(dict):
    def __init__(self, n):
        super(PrimeDecomposition, self).__init__(primes.decomposeProduct(n))

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except:
            return 0

    def __mul__(self, other):
        keys = list(sorted(set(list(self.keys()) + list(other.keys()))))
        product = {key: self[key] + other[key] for key in keys}
        output = PrimeDecomposition(1)
        super(PrimeDecomposition, output).__init__(product)
        output.cleanZeroes()
        return output

    def __pow__(self, power, modulo=None):
        powed = {key: self[key]*power for key in self}
        output = PrimeDecomposition(1)
        super(PrimeDecomposition, output).__init__(powed)
        return output

    def __truediv__(self, other):
        other = other**-1
        return self*other

    def value(self):
        try:
            factors = [key**self[key] for key in self]
            return reduce(mul, factors)
        except:
            return 1

    def cleanZeroes(self):
        keys = list(self.keys())
        for key in keys:
            if self[key] == 0:
                self.pop(key)

    @staticmethod
    def factorial(n):
        if n in (0,1):
            return PrimeDecomposition(1)
        else:
            return PrimeDecomposition(n)*PrimeDecomposition.factorial(n-1)

    @staticmethod
    def pascalCoefficient(k, n):
        return PrimeDecomposition.factorial(n)/(PrimeDecomposition.factorial(n-k)*PrimeDecomposition.factorial(k))