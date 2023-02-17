from math import sqrt, log, floor


def sum_of_even_fibonacci_numbers(limit=4000000):
    golden_ratio = (1 + sqrt(5)) / 2
    n = floor(log(sqrt(5) * limit) / log(golden_ratio))
    fn = round((golden_ratio ** (n + 2)) / sqrt(5))

    return (fn - 1) // 2


if __name__ == "__main__":
    print(sum_of_even_fibonacci_numbers())
