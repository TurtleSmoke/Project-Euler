# Dynamic programming

The problems is a variation of the [Coins sums](https://projecteuler.net/problem=31) problem.
The only difference is the number of coins, which is now prime numbers.
With trial and error, setting the limit to 100 is enough to get the correct answer.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0077/solution1.py):

```python
def prime_summations(n=100):
    numbers = list(sieve.primerange(1, n + 1))
    cache = [1] + [0] * n

    for number in numbers:
        for i in range(number, n + 1):
            cache[i] += cache[i - number]

    return next(i for i, x in enumerate(cache) if x > 5000)
```
