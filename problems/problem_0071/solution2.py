def ordered_fractions(limit=1000000):
    a, b = 2, 5
    c, d = 3, 7

    while b + d <= limit:
        a, b = a + c, b + d

    return a


if __name__ == "__main__":
    print(ordered_fractions())
