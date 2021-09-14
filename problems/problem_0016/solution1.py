def power_digit_sum(n=1000):
    return sum((int(d) for d in str(2**n)))


if __name__ == "__main__":
    print(power_digit_sum())
