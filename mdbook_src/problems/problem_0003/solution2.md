# Two by Two

Since all primes except 2 are odd and in our case 2 is not a factor of
600851475143, we can start with 3 and iterate two by two, which is not a great
improvement, but this problem has no interesting solution anyway.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0003/solution2.py):

```python
def largest_prime_factor(n=600851475143):
    res = 3
    while n != 1:
        if n % res == 0:
            n //= res
        else:
            res += 2

    return res
```