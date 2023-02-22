def is_bin_palindrome(n):
    is_palindrome = lambda s: s == s[::-1]
    return is_palindrome(str(bin(n)[2:]))


def make_palindrome():
    left = 1
    while left < 1000:
        yield int(str(left) + str(left)[::-1][1:])  # Odd length palindromes
        yield int(str(left) + str(left)[::-1])  # Even length palindromes
        left += 1


def double_base_palindromes():
    return sum(n for n in make_palindrome() if is_bin_palindrome(n))


if __name__ == "__main__":
    print(double_base_palindromes())
