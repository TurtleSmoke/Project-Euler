def sum_of_even_fibonacci_numbers(limit=4000000):
    f0 = 1
    f1 = 2
    res = 0
    while f0 < limit:
        if f0 % 2 == 0:
            res += f0
        f0, f1 = f1, f0 + f1

    return res


if __name__ == "__main__":
    print(sum_of_even_fibonacci_numbers())
