def ordered_fractions(limit=1000001):
    res = 0, 1
    for n in range(1, limit):
        for d in range(1, limit):
            if res[0] / res[1] < n / d < 3 / 7:
                res = n, d
    return res[0]


if __name__ == "__main__":
    print(ordered_fractions())
