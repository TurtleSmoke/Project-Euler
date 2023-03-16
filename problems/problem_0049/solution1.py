from sympy import isprime


def prime_permutations():
    for i in range(1000, 10000):
        if i == 1487:
            continue
        for j in range(1, (10000 - i) // 2):
            if (
                isprime(i)
                and isprime(i + j)
                and isprime(i + 2 * j)
                and sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + 2 * j))
            ):
                return str(i) + str(i + j) + str(i + 2 * j)


if __name__ == "__main__":
    print(prime_permutations())
