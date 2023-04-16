import itertools
from math import sqrt


def diophantine_equation():
    res = 0
    for d in range(2, 1001):
        if sqrt(d).is_integer():
            continue

        for x in itertools.count(2):
            if (sqrt((x**2 - 1) / d)).is_integer():
                res = max(res, x)
                break

    return res


if __name__ == "__main__":
    print(diophantine_equation())
