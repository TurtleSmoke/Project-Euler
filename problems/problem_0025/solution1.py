def thousandth_digit_fibonacci_number(n=1000):
    f1 = 1
    f2 = 1
    res = 1
    while len(str(f1)) < n:
        f1, f2 = f2, f1 + f2
        res += 1

    return res


if __name__ == "__main__":
    print(thousandth_digit_fibonacci_number())
