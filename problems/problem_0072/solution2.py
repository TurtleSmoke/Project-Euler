def counting_fractions(n=1000000):
    tlist = list(range(n + 1))

    for i in range(1, n + 1):
        p = tlist[i]
        for j in range(2 * i, n + 1, i):
            tlist[j] -= p

    return sum(tlist) - 1


if __name__ == "__main__":
    print(counting_fractions())
