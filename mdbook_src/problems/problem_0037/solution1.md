# Brute force

To solve the problem of finding truncatable primes, we will use Python's slicing again to check whether the left and right slices of a number are prime.
Using the [all](https://docs.python.org/3/library/functions.html#all) function, we can check both slices at once efficiently.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0037/solution1.py):

```python
def is_truncatable_prime(n):
    return all(isprime(int(n[i:])) and isprime(int(n[:i])) for i in range(1, len(n)))
```

Since the problem states that there are only eleven primes, we don't need to set an upper bound for our iteration.
We can use [itertools.count](https://docs.python.org/3/library/itertools.html#itertools.count) to make the code more concise.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0037/solution1.py):

```python
def truncatable_primes():
    res = []
    for i in itertools.count(10):
        if isprime(i) and is_truncatable_prime(str(i)):
            res.append(i)
            if len(res) == 11:
                return sum(res)
```
