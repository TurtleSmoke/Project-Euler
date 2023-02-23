from sympy import isprime


def is_left_truncatable(n):
    return all(isprime(int(n[i:])) for i in range(1, len(n)))


def construct_truncatable_primes(num):
    if isprime(num):
        if num > 10 and num % 10 in (3, 7) and is_left_truncatable(str(num)):
            yield num
        for new_digit in (1, 3, 7, 9):
            yield from construct_truncatable_primes(num * 10 + new_digit)


def truncatable_primes():
    return sum(sum(construct_truncatable_primes(d)) for d in (2, 3, 5, 7))


if __name__ == "__main__":
    print(truncatable_primes())
