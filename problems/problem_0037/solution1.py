import itertools

from sympy import isprime


def is_truncatable_prime(n):
    return all(isprime(int(n[i:])) and isprime(int(n[:i])) for i in range(1, len(n)))


def truncatable_primes():
    res = []
    for i in itertools.count(10):
        if isprime(i) and is_truncatable_prime(str(i)):
            res.append(i)
            if len(res) == 11:
                return sum(res)


if __name__ == "__main__":
    print(truncatable_primes())
