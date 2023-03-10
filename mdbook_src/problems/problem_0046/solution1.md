# Brute force

The brute force approach for determining the minimal odd composite number that does not satisfy the Goldbach's other conjecture can be separated into two steps:

- Verify whether a number satisfies the Goldbach's other conjecture.
- Iterate through all odd composite numbers.

The first step can be brute force by iterating through every \\( i \leq n \\) and verify if \\( i \\) is prime and \\( \sqrt{\frac{n-i}{2}} \\) is an integer.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0046/solution1.py):

```python
def is_odd_goldbach(n):
    return any(isprime(i) and (((n - i) / 2) ** 0.5).is_integer() for i in range(1, n + 1))
```

Assuming the existence of a solution, the second part is straightforward and can be done by iterating through all odd composite numbers until a solution is found.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0046/solution1.py):

```python
def goldbachs_other_conjecture():
    for i in itertools.count(7, 2):
        if not is_odd_goldbach(i):
            return i
```
