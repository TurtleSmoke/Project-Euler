# Shorten the intervals

If with take a closer look at the equation, we should find useful information.
For example, with some peculiar values of \\( n \\), we can narrow down the
ranges of \\( a \\) and \\( b \\).

We are searching \\( p \\) prime such that:

\\[ p = n^2 + an + b \\]

For \\( n = 0\\), the equation is \\( p = b \\). That means that \\( b \\)
must be a prime.

For \\( n = b \\), the equation is \\( p = b^2 + ab + b = b(b + a + 1) \\)
which is divisible by \\( b \\). \\( b \\) is in fact the limit of consecutive
primes that can be found using this equation.

Rearranging the equation we have:

\\[ p = n^2 + an + b \Leftrightarrow p - b = n(n + a) \\]

Since both \\( p \\) and \\( b \\) are prime, \\( p - b \\) is an even number.

If \\( n \\) is even then \\( n(n + a) \\) will also be even.\
If \\( n \\) is odd, then \\( n(n + a) \\) will be odd only if \\( a \\) is odd.

For \\( n = 1 \\), \\( n^2 + an + b \\) will never be a prime if \\( a \\) is
even.

All this information can help quite a bit:

* \\( a \\) must be an odd number between.
* b must be a prime.
* b is the upper limit of consecutive primes.

```python
def quadratic_primes():
    primes_b = list((primerange(0, 1000)))[::-1]  # b is prime.
    res = 0
    max_primes = 0
    for a in range(-999, 1000, 2):  # a is odd.
        for b in primes_b:
            if b < max_primes:  # b is the limit for consecutive prime.
                continue

            n = 0
            while isprime(n ** 2 + a * n + b):
                n += 1

            if n > max_primes:
                max_primes = n
                res = a * b

    return res
```