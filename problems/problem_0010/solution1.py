from sympy import sieve


def summation_of_primes(limit=2000000):
    return sum(sieve.primerange(limit))


if __name__ == "__main__":
    print(summation_of_primes())
