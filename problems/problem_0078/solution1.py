def coin_partitions(limit=100000):
    divisible_by = 1000000
    cache = [1] * (limit + 1)
    for l in range(2, limit + 1):
        cache[l] = (cache[l] + 1) % divisible_by

        if cache[l] == 0:
            return l

        for n in range(l + 1, limit + 1):
            cache[n] = (cache[n] + cache[n - l]) % divisible_by


if __name__ == "__main__":
    print(coin_partitions())
