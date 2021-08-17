def largest_prime_factor(n=600851475143):
    res = 2
    while n != 1:
        if n % res == 0:
            n //= res
        else:
            res += 1
    return res


if __name__ == "__main__":
    print(largest_prime_factor())
