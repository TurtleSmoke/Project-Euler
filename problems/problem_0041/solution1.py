import itertools

from sympy import isprime


def pandigital_prime():
    initial = "987654321"
    while True:
        for s in itertools.permutations(initial):
            n = int("".join(s))
            if isprime(n):
                return n
        initial = initial[1:]


if __name__ == "__main__":
    print(pandigital_prime())
