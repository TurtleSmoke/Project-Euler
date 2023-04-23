def totient_list(n):
    tlist = list(range(n))
    for i in range(1, n):
        p = tlist[i]
        for j in range(2 * i, n, i):
            tlist[j] -= p
    return tlist


def totient_maximum(limit=1000001):
    res = 0
    res_n = 0
    totatives = totient_list(limit)
    for n in range(2, limit):
        if n / totatives[n] > res:
            res = n / totatives[n]
            res_n = n
    return res_n


if __name__ == "__main__":
    print(totient_maximum())
