def coin_sums(n=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n + 1):
            cache[i] += cache[i - coin]

    return cache[-1]


if __name__ == "__main__":
    print(coin_sums(200))
