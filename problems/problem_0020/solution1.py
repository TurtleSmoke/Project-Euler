from math import factorial


def factorial_digit_sum(n=100):
    return sum(int(x) for x in str(factorial(n)))


if __name__ == "__main__":
    print(factorial_digit_sum())
