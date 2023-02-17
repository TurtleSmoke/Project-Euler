from math import floor, sqrt


def get_sum_of_factors(n):
    sum_of_factors = [1] * (n + 1)
    for i in range(2, floor(sqrt(n)) + 1):
        sum_of_factors[i * i] += i
        for j in range(i + 1, (n // i) + 1):
            sum_of_factors[i * j] += i + j

    return sum_of_factors


def non_abundant_sums(n=28123):
    sum_of_factors = get_sum_of_factors(n)
    abundant = set()
    res = 0

    for i in range(1, n + 1):
        if sum_of_factors[i] > i:
            abundant.add(i)
        if all((i - a1 not in abundant) for a1 in abundant):
            res += i

    return res


if __name__ == "__main__":
    print(non_abundant_sums())
