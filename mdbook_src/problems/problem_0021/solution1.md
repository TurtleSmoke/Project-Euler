# Brute force

The problem first requires to find the sum of proper divisors of a number, if
recall, in the
[Problem 12: Highly divisible triangular number](../problem_0012/problem.md), we
found the number of proper divisors, we can reuse this function by adding the
divisors rather than counting them.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0021/solution1.py):

```python
def sum_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            res += i + n // i

    return res
```

We can simply iterate from 1 to 10000 and sum the amicable numbers found to find
the solution, we just to be aware that even if \\( d(6) = 6 \\) and so \\( d(6)
= 6 \\), 6 is not an amicable number because amicable numbers are in pairs.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0021/solution1.py):

```python
def amicable_numbers(n=10000):
    res = 0
    for i in range(2, n):
        current = sum_of_factors(i)
        if i != current and i == sum_of_factors(current):
            res += i

    return res
```
