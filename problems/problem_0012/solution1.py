def number_of_factors(n):
    res = 1
    for i in range(2, n):
        if n % i == 0:
            res += 1
    return res


def highly_div_triangular_number(n=500):
    i = 1
    res = 1
    while number_of_factors(res) < n:
        i += 1
        res += i

    return res


if __name__ == "__main__":
    print(highly_div_triangular_number())
