from math import floor, sqrt


def non_abundant_sums(n=28123):
    sum_of_factors = [1] * (n + 1)
    for i in range(2, floor(sqrt(n)) + 1):
        sum_of_factors[i * i] += i
        for j in range(i + 1, (n // i) + 1):
            sum_of_factors[i * j] += i + j

    abundants = set()
    res = 0

    for i in range(1, n + 1):
        if sum_of_factors[i] > i:
            abundants.add(i)
        if not any((i - a1 in abundants) for a1 in abundants):
            res += i

    return res


if __name__ == "__main__":
    print(non_abundant_sums())
