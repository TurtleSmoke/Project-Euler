def collatz(n):
    iteration = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        iteration += 1

    return iteration


def longest_collatz_sequence(n=1000000):
    res, max_it = 0, 0
    for i in range(1, n):
        current_it = collatz(i)
        if current_it > max_it:
            res, max_it = i, current_it

    return res


if __name__ == "__main__":
    print(longest_collatz_sequence())
