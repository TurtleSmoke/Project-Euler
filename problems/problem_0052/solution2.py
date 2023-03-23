import itertools


def permuted_multiples():
    for i in itertools.count(100008, 9):  # Observation 1 and 4
        s = str(i)
        if int(s[0]) != 1 or all(d not in s for d in "05"):  # Observation 2 and 3
            continue
        if all(sorted(s) == sorted(str(i * j)) for j in range(2, 7)):
            return i


if __name__ == "__main__":
    print(permuted_multiples())
