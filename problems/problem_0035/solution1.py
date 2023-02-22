from sympy import isprime


def is_circular_prime(n):
    return all(isprime(int(n[i:] + n[:i])) for i in range(len(n)))


def circular_primes():
    return sum(is_circular_prime(str(i)) for i in range(2, 1000000))


if __name__ == "__main__":
    print(circular_primes())
