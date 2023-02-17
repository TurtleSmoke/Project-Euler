from sympy import isprime
from sympy import primerange


def quadratic_primes():
    primes_b = list((primerange(0, 1000)))[::-1]  # b is prime.
    res = 0
    max_primes = 0
    for a in range(-999, 1000, 2):  # a is odd.
        for b in primes_b:
            if b < max_primes:  # b is the limit for consecutive prime.
                continue

            n = 0
            while isprime(n**2 + a * n + b):
                n += 1

            if n > max_primes:
                max_primes = n
                res = a * b

    return res


if __name__ == "__main__":
    print(quadratic_primes())
