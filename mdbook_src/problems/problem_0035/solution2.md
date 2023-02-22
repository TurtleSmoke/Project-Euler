# 1, 3, 7, 9

It is possible to reduce the number of candidate numbers that need to be checked for circular primality by taking into account that prime numbers cannot end with the digits 0, 2, 4, 5, 6 or 8.
Therefore, numbers containing these digits can be skipped from consideration.

By using the [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product),
it is possible to generate all possible combinations of the digits 1, 3, 7 and 9.
This approach reduces the number of potential circular prime to less than 6,000,
rather than the previous 1,000,000.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0035/solution2.py):

```python
def circular_primes():
    res = 4
    for number_digits in range(2, 7):
        for n in itertools.product('1379', repeat=number_digits):
            if is_circular_prime(''.join(n)):
                res += 1
    return res
```

Although the current solution is effective, it's possible to further optimize the solution.
For instance, since we check all circular permutations of a given number, we may be checking the same number multiple times.
Additionally, we know that all prime numbers can be expressed as either \\( 6n+1 \\) or \\( 6n-1 \\).
However, implementing these optimizations may not be worthwhile.