# Brute force

The problem is to find the value of \\( D \leq 1000 \\) for which \\( x \\) is maximised in the equation \\( x^2 - Dy^2 = 1 \\).

Brute forcing the solution is easy, for each \\( D \leq 1000 \\) that is not a perfect square, and for each \\( x > 1 \\), if \\( y = \sqrt{\frac{x^2 - 1}{D}} \\) is an integer, then \\( x^2 - Dy^2 = 1 \\) is satisfied.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0066/solution1.py):

```python
def diophantine_equation():
    res = 0
    for d in range(2, 1001):
        if sqrt(d).is_integer():
            continue

        for x in itertools.count(2):
            if (sqrt((x**2 - 1) / d)).is_integer():
                res = max(res, x)
                break

    return res
```

However, the brute force approach is not effective and does not provide the solution for \\( D = 61 \\) as \\( x \\) becomes too large...