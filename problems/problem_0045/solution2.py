def is_pentagonal(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()


def hn(n):
    return n * (2 * n - 1)


def triangular_pentagonal_and_hexagonal():
    h = 145
    while not is_pentagonal(hn(h)):
        h += 1
    return hn(h)


if __name__ == "__main__":
    print(triangular_pentagonal_and_hexagonal())
