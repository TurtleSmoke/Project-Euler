import itertools


def is_pentagonal(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()


def pentagon_numbers():
    res = float("inf")
    pn = lambda n: n * (3 * n - 1) // 2
    for i in itertools.count(2):
        if 3 * i + 1 > res:
            break
        for j in range(i - 1, 0, -1):
            a = pn(i)
            b = pn(j)
            if a - b > res:
                break
            if is_pentagonal(a + b) and is_pentagonal(a - b) and a - b < res:
                res = a - b
    return res


if __name__ == "__main__":
    print(pentagon_numbers())
