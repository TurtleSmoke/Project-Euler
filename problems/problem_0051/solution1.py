import itertools

from sympy import isprime, sieve


def is_nth_prime_value_family(n):
    for mask in itertools.product([False, True], repeat=len(n)):
        seq_len = 0
        res = 0
        for d in "0123456789":
            if mask[0] and d == "0" or not any(mask):
                continue
            first = int("".join((d if mask[j] else n[j] for j in range(len(n)))))
            if isprime(first):
                if seq_len == 0:
                    res = first

                seq_len += 1
                if seq_len == 8:
                    return res
    return None


def prime_digit_replacements():
    for i in sieve:
        res = is_nth_prime_value_family(str(i))
        if res is not None:
            return res


# 5 -> 56003
# 4 -> 2207
# 3 -> 107
# 3 -> 13
if __name__ == "__main__":
    print(prime_digit_replacements())
