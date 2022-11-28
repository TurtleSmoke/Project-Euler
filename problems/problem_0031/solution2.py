def coin_sums(n=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [[1] + [0] * (len(coins) - 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(1, len(coins)):
            cache[i][j] = cache[i][j - 1]
            if coins[j] <= i:
                cache[i][j] += cache[i - coins[j]][j]

    return cache[-1][-1]


if __name__ == "__main__":
    print(coin_sums(200))
