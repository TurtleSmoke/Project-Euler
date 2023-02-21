def is_criterion(x):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return x == sum(facts[int(i)] for i in str(x))


def digit_factorials():
    return sum(i for i in range(3, 7 * 362880) if is_criterion(i))


if __name__ == "__main__":
    print(digit_factorials())
