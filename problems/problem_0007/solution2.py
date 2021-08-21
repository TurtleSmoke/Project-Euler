def n_th_prime(n=10001):
    i = 1
    primes = [2, 3]
    while len(primes) < n:
        if all((6 * i - 1) % p != 0 for p in primes):
            primes.append(6 * i - 1)
        if all((6 * i + 1) % p != 0 for p in primes):
            primes.append(6 * i + 1)
        i += 1

    return primes[n - 1]


if __name__ == "__main__":
    print(n_th_prime())
