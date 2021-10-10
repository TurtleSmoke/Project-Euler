from math import ceil, log10, sqrt


def thousandth_digit_fibonacci_number(n=1000):
    return ceil((n - 1 + log10(sqrt(5)) / 2) / log10((1 + sqrt(5)) / 2))


if __name__ == "__main__":
    print(thousandth_digit_fibonacci_number())
