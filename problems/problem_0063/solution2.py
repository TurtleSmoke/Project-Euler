from math import log10, floor


def powerful_digit_counts():
    return sum(floor(1 / (1 - log10(i))) for i in range(1, 10))


if __name__ == "__main__":
    print(powerful_digit_counts())
