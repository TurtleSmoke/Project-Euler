def is_double_palindrome(n):
    is_palindrome = lambda s: s == s[::-1]
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])


def double_base_palindromes():
    return sum(n for n in range(1000000) if is_double_palindrome(n))


if __name__ == "__main__":
    print(double_base_palindromes())
