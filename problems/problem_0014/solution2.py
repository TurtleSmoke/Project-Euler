def longest_collatz_sequence(n=1000000):
    cache = {1: 1}

    def collatz(i):
        if i not in cache:
            cache[i] = collatz(i // 2 if i % 2 == 0 else 3 * i + 1) + 1

        return cache[i]

    return max(range(1, n), key=collatz)


if __name__ == "__main__":
    print(longest_collatz_sequence())
