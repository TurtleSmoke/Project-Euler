# Brute force

The problem is to find the maximum reduced proper fraction \\( \frac{n}{d} < \frac{3}{7} \\) with \\( n < d \leq 1000000 \\).

The brute force approach iterate over every \\( n \\) and \\( d \\) and find the maximum fraction that satisfies the condition.
There is no need to reduce the fraction since the iteration is ascending and the reduced fraction will be found first.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0071/solution1.py):

```python
def ordered_fractions(limit=1000001):
    res = 0, 1
    for n in range(1, limit):
        for d in range(1, limit):
            if res[0] / res[1] < n / d < 3 / 7:
                res = n, d
    return res[0]
```
