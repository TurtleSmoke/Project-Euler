from math import floor, sqrt


def quadratic_primes(limit=1000):
    l = floor((-1 + sqrt(1 - 4 * (41 - limit))) / 2)
    return (l ** 2 + l + 41) * (-(2 * l + 1))


if __name__ == "__main__":
    print(quadratic_primes())
