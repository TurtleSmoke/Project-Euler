from math import factorial


def lexicographic_permutations(s, n):
    if len(s) <= 1:
        return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + lexicographic_permutations(s[:q] + s[q + 1 :], r)


if __name__ == "__main__":
    print(lexicographic_permutations("0123456789", 999999))
