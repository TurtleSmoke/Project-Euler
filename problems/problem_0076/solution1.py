def counting_summations(n=100):
    numbers = list(range(1, n))
    cache = [1] + [0] * n

    for number in numbers:
        for i in range(number, n + 1):
            cache[i] += cache[i - number]

    return cache[-1]


if __name__ == "__main__":
    print(counting_summations())
