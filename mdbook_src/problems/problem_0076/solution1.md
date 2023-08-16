# Dynamic programming

The problems is a variation of the [Coins sums](https://projecteuler.net/problem=31) problem.
The only difference is the number of coins, which is now 1, 2, 3, ..., 99.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0076/solution1.py):

```python
def counting_summations(n=100):
    numbers = list(range(1, n))
    cache = [1] + [0] * n

    for number in numbers:
        for i in range(number, n + 1):
            cache[i] += cache[i - number]

    return cache[-1]
```
