import itertools

from sympy import isprime


def is_circular_prime(n):
    return all(isprime(int(n[i:] + n[:i])) for i in range(len(n)))


def circular_primes():
    res = 4
    for number_digits in range(2, 7):
        for n in itertools.product("1379", repeat=number_digits):
            if is_circular_prime("".join(n)):
                res += 1
    return res


if __name__ == "__main__":
    print(circular_primes())
