from math import sqrt, ceil


def partial_prime_sum(n=2000000):
    r = ceil(sqrt(n))
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i: i * (i + 1) // 2 - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:  # p is prime
            sp = S[p - 1]  # sum of primes smaller than p
            p2 = p * p
            for v in V:
                if v < p2:
                    break
                S[v] -= p * (S[v // p] - sp)
    return S[n]


if __name__ == "__main__":
    print(partial_prime_sum())
