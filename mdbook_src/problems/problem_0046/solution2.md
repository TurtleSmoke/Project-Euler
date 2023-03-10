# Better iteration and caching

The [Brute force](./solution1.md) approach is fast enough because the solution is small.
But the function that determines whether a number satisfies the Goldbach's other conjecture can be further optimized.

The key is to iterate through all double squares \\( 2i^2 \\) with \\( i \leq \sqrt{\frac{n}{2}} \\) and check whether \\(n - 2i^2 \\) is prime.
Additionally, a cache of prime numbers can be used and updated when a new prime number is found.
New primes can only be found if \\( n \\) is prime, because \\( n - 2i^2 \\) prime implies that a previous composite number was prime.
Thus, the cache is updated if \\( n \\) is prime, if not, it can be used to determine whether \\( n - 2i^2 \\) is prime.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0046/solution2.py):

```python
def is_odd_goldbach(n, primes_cache):
    if isprime(n):
        primes_cache.add(n)
        return True

    return any(n - 2 * i**2 in primes_cache for i in range(1, int(n**0.5) + 1))
```

The rest stays the same.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0046/solution2.py):

```python
def goldbachs_other_conjecture():
    primes_cache = {2, 3, 5}
    for i in itertools.count(7, 2):
        if not is_odd_goldbach(i, primes_cache):
            return i
```
