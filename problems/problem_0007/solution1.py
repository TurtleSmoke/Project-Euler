def n_th_prime(n=10001):
    i = 3
    primes = [2]
    while len(primes) < n:
        if all(i % p != 0 for p in primes):  # No divisor in the previous prime.
            primes.append(i)
        i += 2

    return primes[-1]


if __name__ == "__main__":
    print(n_th_prime())
