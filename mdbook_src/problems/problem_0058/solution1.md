# Brute force

This problem should reminisce you of [Problem 28](../problem_0028/problem.md).
Utilizing information from the previous problem, the solution becomes straightforward and involves iterating through each value in the corner until the ratio of primes falls below 10%.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0058/solution1.py):

```python
def spiral_primes():
    res = 0
    for i in itertools.count(3, 2):
        res += (
            isprime(i**2) + isprime(i**2 - (i - 1)) + isprime(i**2 - 2 * (i - 1)) + isprime(i**2 - 3 * (i - 1))
        )
        if res < (2 * i - 1) / 10:
            return i
```
