import itertools
from math import sqrt, floor


def period_square_roots(n):
    a_0 = floor(sqrt(n))
    if a_0 * a_0 == n:
        return 0

    bn = a_0
    cn = 1

    for pos in itertools.count(1):
        cn = (n - (bn * bn)) / cn
        an = floor((sqrt(n) + bn) / cn)
        bn = -(bn - (an * cn))
        if an == 2 * a_0:
            return pos


def odd_period_square_roots():
    return sum(period_square_roots(n) % 2 for n in range(2, 10001))


if __name__ == "__main__":
    print(odd_period_square_roots())
