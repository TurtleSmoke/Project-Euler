# Brute force

The problem is to find the value of \\( n \\) for which \\( \frac{n}{\phi(n)} \\) is a maximum.

The naive approach is to compute \\( \phi(n) \\) for all \\( n \\) up to \\( 1,000,000 \\) and then find the maximum value of \\( \frac{n}{\phi(n)} \\).
\\( \phi(n) \\) can be computed by summing the count of coprimes numbers of \\( n \\) up to \\( n - 1 \\).

Two numbers are considered coprime if their greatest common divisor is \\( 1 \\), indicating that they have no common factors.
Checking for coprime numbers can be done by verifying if there exists any number that is a factor of both numbers in the range from \\( 1 \\) to \\( \min(a, b) \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0069/solution1.py):

```python
def are_coprime(a, b):
    return not any(a % i == 0 and b % i == 0 for i in range(2, min(a, b) + 1))
```

Finally, the rest is to compute \\( \frac{n}{\phi(n)} \\) for all \\( n \\) up to \\( 1,000,000 \\) and find the maximum value.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0069/solution1.py):

```python
def totient_maximum():
    res = 0
    res_n = 0
    for n in range(2, 1000001):
        totient = sum(are_coprime(n, i) for i in range(1, n))
        res = max(res, n / totient)
        if n / totient > res:
            res = n / totient
            res_n = n
    return res_n
```
