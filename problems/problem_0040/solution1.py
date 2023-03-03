import operator
from functools import reduce


def champernownes_constant():
    s = "".join(str(i) for i in range(1, 1000000))
    print([int(s[10**i - 1]) for i in range(7)])
    return reduce(operator.mul, (int(s[10**i - 1]) for i in range(7)))


if __name__ == "__main__":
    print(champernownes_constant())
