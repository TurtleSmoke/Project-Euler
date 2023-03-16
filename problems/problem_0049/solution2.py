from collections import defaultdict

from sympy import sieve


def prime_permutations():
    primes = list(sieve.primerange(1000, 10000))
    primes_permutations = defaultdict(list)
    for prime in primes:
        primes_permutations["".join(sorted(str(prime)))].append(prime)

    for perm in primes_permutations.values():
        if len(perm) < 3 or perm[0] == 1487:
            continue

        for i, p1 in enumerate(perm):
            for p2 in perm[i + 1 :]:
                p3 = 2 * p2 - p1
                if p3 in perm:
                    return str(p1) + str(p2) + str(p3)


if __name__ == "__main__":
    print(prime_permutations())
