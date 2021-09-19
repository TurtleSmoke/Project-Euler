from math import floor, sqrt


def sum_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            res += i + n // i

    return res


def amicable_numbers(n=10000):
    res = 0
    for i in range(2, n):
        current = sum_of_factors(i)
        if i != current and i == sum_of_factors(current):
            res += i

    return res


if __name__ == "__main__":
    print(amicable_numbers())
