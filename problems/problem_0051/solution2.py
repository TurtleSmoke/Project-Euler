from sympy import sieve, isprime


def is_nth_prime_value_family(n):
    for d in range(3):  # Observation 2
        mask = 0
        occurrences = 0
        for i, m in enumerate(str(n)[::-1]):  # Reverse string for easier mask creation
            if m == str(d):
                mask += 10**i
                occurrences += 1

        if occurrences == 0 or occurrences % 3 != 0:  # Observation 3
            continue

        seq_len = 0
        for r in range(10 - d):
            if seq_len + 10 - r < 8:  # Observation 2
                break
            if isprime(n + r * mask):  # Observation 4
                seq_len += 1
            if seq_len == 8:
                return n


def prime_digit_replacements():
    for i in sieve:
        res = is_nth_prime_value_family(i)
        if res is not None:
            return res


# 5 -> 56003
# 4 -> 2207
# 3 -> 107
# 3 -> 13
if __name__ == "__main__":
    print(prime_digit_replacements())
