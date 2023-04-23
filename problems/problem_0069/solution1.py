def are_coprime(a, b):
    return not any(a % i == 0 and b % i == 0 for i in range(2, min(a, b) + 1))


def totient_maximum():
    res = 0
    res_n = 0
    for n in range(2, 1000001):
        totient = sum(are_coprime(n, i) for i in range(1, n))
        res = max(res, n / totient)
        if n / totient > res:
            res = n / totient
            res_n = n
    return res_n


if __name__ == "__main__":
    print(totient_maximum())
