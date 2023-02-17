from math import floor, sqrt


def sum_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            res += i + n // i

    if root**2 == n:
        res -= root

    return res


def is_sum(i, abundant):
    return any(a1 + a2 == i for a1 in abundant for a2 in abundant)


def non_abundant_sums():
    abundant = [i for i in range(1, 28124) if sum_of_factors(i) > i]

    return sum(i for i in range(28124) if not is_sum(i, abundant))


if __name__ == "__main__":
    print(non_abundant_sums())
