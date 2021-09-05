from math import sqrt, floor


def number_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root):
        if n % i == 0:
            res += 1
    return 2 * res + (root**2 == n)


def highly_div_triangular_number(n=500):
    i = 0
    factors = 0
    while factors < n:
        i += 1
        if i % 2 == 0:
            factors = number_of_factors(i // 2) * number_of_factors(i + 1)
        else:
            factors = number_of_factors(i) * number_of_factors((i + 1) // 2)

    return i * (i + 1) // 2


if __name__ == "__main__":
    print(highly_div_triangular_number())
