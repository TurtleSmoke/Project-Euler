# Brute force

The problem is to find the best combination of \\( a \\) and \\( b \\) such that
the formula:

\\[ n^2 + an + b \\]

produces the largest number of primes for consecutive values of \\( n \\). The
absolute value of \\( a \\) and \\( b \\) must be less than \\( 1000 \\).

The brute force solution is to iterate from \\( -1000 \\) to \\( 1000 \\)
for \\( a \\) and \\( b \\) and count the number of consecutive primes each
time.

```python
def quadratic_primes(limit=1000):
    res = 0
    max_primes = 0
    for a in range(-limit, limit):
        for b in range(-limit, limit):
            n = 0
            while isprime(n ** 2 + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                res = a * b

    return res
```