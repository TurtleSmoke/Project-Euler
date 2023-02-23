import itertools


def is_pandigital_multiples(seed):
    digits = str(seed)
    for j in itertools.count(2):
        digits += str(seed * j)
        if len(digits) > 9:
            return -1
        if len(digits) == 9 and set(digits) == set("123456789"):
            return int(digits)


def pandigital_multiples():
    return max(is_pandigital_multiples(seed) for seed in range(1, 10000))


if __name__ == "__main__":
    print(pandigital_multiples())
