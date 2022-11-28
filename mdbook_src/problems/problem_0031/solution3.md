# Better dynamic programming

Dynamic programming can be a bit improved by using a single array instead of a
table. The array will contain the number of ways to make \\( n \\) using the
coins we have. The array will be initialized with 1, and we will update it by
adding the number of ways to make \\( n - c \\) to the current value. This way
we will only need \\( O(n) \\) space. The time complexity will be the same
as the previous solution, but the space complexity will be better.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0031/solution3.py):

```python
def coin_sums(n=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [1] + [0] * n

    for coin in coins:
        for i in range(coin, n + 1):
            cache[i] += cache[i - coin]

    return cache[-1]
```
