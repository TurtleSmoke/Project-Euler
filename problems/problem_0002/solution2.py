def sum_of_even_fibonacci_numbers(limit=4000000):
    e0 = 0
    e1 = 2
    while e1 < limit:
        e0, e1 = e1, 4 * e1 + e0
    return (e1 + e0 - 2) // 4


if __name__ == "__main__":
    print(sum_of_even_fibonacci_numbers())
