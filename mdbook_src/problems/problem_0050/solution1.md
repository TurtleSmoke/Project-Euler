# Brute force

To solve the problem of finding the prime number below one million that can be expressed as the longest sum of consecutive primes, the first idea is to generate all the primes below one million.
Subsequently, brute-forcing all possible combinations of consecutive primes can be evaluated to identify the longest sequence whose sum is also a prime.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0050/solution1.py):

```python
def consecutive_prime_sum(lim=10**6):
    primes = list(sieve.primerange(2, lim))
    res = 0
    max_len = 0
    for i in range(len(primes)):
        for j in range(i + max_len, len(primes)):
            s = sum(primes[i:j])
            if s >= lim:
                break
            if j - i > max_len and s in primes:
                max_len = j - i
                res = s
    return res
```
