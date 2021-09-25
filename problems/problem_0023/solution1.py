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


def non_abundant_sums():
    abundants = [i for i in range(1, 28124) if sum_of_factors(i) > i]
    is_sum = lambda i: any(a1 + a2 == i for a1 in abundants for a2 in abundants)

    return sum(i for i in range(28124) if not is_sum(i))


if __name__ == "__main__":
    print(non_abundant_sums())
