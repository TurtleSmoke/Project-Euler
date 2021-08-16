import math


def sum_of_even_fibonacci_numbers(limit=4000000):
    golden_ratio = (1 + math.sqrt(5)) / 2
    n = math.floor(math.log(math.sqrt(5) * limit) / math.log(golden_ratio))

    fn = round((golden_ratio**(n + 2)) / math.sqrt(5))

    return (fn - 1) // 2


if __name__ == "__main__":
    print(sum_of_even_fibonacci_numbers())
