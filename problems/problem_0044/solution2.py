import itertools


def is_pentagonal(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()


def pn(n):
    return n * (3 * n - 1) // 2


def pentagon_numbers():
    for d in itertools.count(4):
        pd = pn(d)
        for x in range(d - 3, 0, -3):
            px = pn(x)
            if (pd - px) % (3 * x) == 0:
                j = (pd - px) // (3 * x)
                k = x + j
                if is_pentagonal(pn(k) + pn(j)):
                    return pd


if __name__ == "__main__":
    print(pentagon_numbers())
