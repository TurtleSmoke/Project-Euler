def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome_product():
    res = 0
    for x in range(110, 1000, 11):
        for y in range(x, 1000):
            if x * y > res and is_palindrome(x * y):
                res = x * y

    return res


if __name__ == "__main__":
    print(largest_palindrome_product())
