from modules.fastPrimalityTest import fastPrimalityTest
from modules.primes import Primes


def powerSet(l: list) -> list:
    if not l:
        yield []
    else:
        for e in powerSet(l[1:]):
            yield e
            yield [l[0]] + e


def digitPositions(n: int) -> list:
    positions = [[] for k in range(10)]
    for position, digit in enumerate(str(n)):
        positions[int(digit)].append(position)
    return positions


def replaceDigitsWith(number: int, positions: list, digit: int) -> int:
    number = list(str(number))
    for position in positions:
        number[position] = str(digit)
    return int("".join(number))


def replaceDigitsWithAllDigit(number: int, positions: list) -> list:
    output = [replaceDigitsWith(number, positions, digit) for digit in range(10)]
    return [e for e in output if len(str(e)) == len(str(number))]


def families(number: int):
    positions = digitPositions(number)
    for i in range(10):
        if positions[i]:
            for replacementPossibility in powerSet(positions[i]):
                if replacementPossibility:
                    yield replaceDigitsWithAllDigit(number, replacementPossibility)


def primesInFamily(family: list) -> list:
    isPrime = lambda n: fastPrimalityTest(n, 10)
    return list(filter(isPrime, family))


def solve(familySize: int = 8) -> int:
    primes = Primes()
    for prime in primes:
        for family in families(prime):
            if len(primesInFamily(family)) == familySize:
                return min(primesInFamily(family))


if __name__ == '__main__':
    print(solve(8))
