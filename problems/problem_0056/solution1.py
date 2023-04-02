def digits_sum(n):
    return sum(map(int, str(n)))


def powerful_digit_sum():
    return max(digits_sum(a**b) for a in range(1, 100) for b in range(1, 100))


if __name__ == "__main__":
    print(powerful_digit_sum())
