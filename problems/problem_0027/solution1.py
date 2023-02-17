from sympy import isprime


def quadratic_primes(limit=1000):
    res = 0
    max_primes = 0
    for a in range(-limit, limit):
        for b in range(-limit, limit):
            n = 0
            while isprime(n**2 + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                res = a * b

    return res


if __name__ == "__main__":
    print(quadratic_primes())
