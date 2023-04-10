import itertools


def powerful_digit_counts():
    res = 0
    for i in range(1, 10):
        for j in itertools.count(1):
            if len(str(i**j)) == j:
                res += 1
            elif len(str(i**j)) < j:
                break
    return res


if __name__ == "__main__":
    print(powerful_digit_counts())
