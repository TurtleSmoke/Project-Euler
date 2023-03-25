from math import factorial


def ncr(n, r):
    return int((factorial(n) / (factorial(r) * factorial(n - r))))


def combinatoric_selections():
    return sum(ncr(n, r) > 1000000 for n in range(23, 101) for r in range(1, n))


if __name__ == "__main__":
    print(combinatoric_selections())
