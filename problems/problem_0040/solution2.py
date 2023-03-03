import operator
from functools import reduce
from math import floor


def d(n):
    s = lambda n: 1 + 9 * sum(i * 10 ** (i - 1) for i in range(1, n))
    digit = 1
    while s(digit) <= n:
        digit += 1
    digit -= 1
    sd = s(digit)
    k = floor((n - sd) / digit)
    number = str(10 ** (digit - 1) + k)
    return int(number[n - (sd + k * digit)])


def champernownes_constant():
    return reduce(operator.mul, (d(10**i) for i in range(7)))


if __name__ == "__main__":
    print(champernownes_constant())
