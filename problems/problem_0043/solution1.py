import itertools


def is_sub_string_divisible(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(int(str(n)[i + 1 : i + 4]) % d == 0 for i, d in enumerate(divisors))


def sub_string_divisibility():
    res = 0
    for i in itertools.permutations("9876543210"):
        if i[0] == "0":
            continue
        x = int("".join(i))
        if is_sub_string_divisible(x):
            res += x
    return res


if __name__ == "__main__":
    print(sub_string_divisibility())
