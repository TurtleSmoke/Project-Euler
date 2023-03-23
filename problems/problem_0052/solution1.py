import itertools


def permuted_multiples():
    for i in itertools.count(1):
        if all(sorted(str(i)) == sorted(str(i * j)) for j in range(2, 7)):
            return i


if __name__ == "__main__":
    print(permuted_multiples())
