def counting_fractions(n=1000001):
    a, b, c, d = 0, 1, 1, n
    res = 0

    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        res += 1

    return res


if __name__ == "__main__":
    print(counting_fractions())
