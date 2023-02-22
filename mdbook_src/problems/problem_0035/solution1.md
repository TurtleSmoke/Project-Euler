# Brute force

Determining whether a number is a circular prime can be achieved by rotating the digits of the number with Python's string slicing functionality, followed by a check for primality.
Instead of a loop, we used the built-in function [all](https://docs.python.org/fr/3/library/functions.html?highlight=all#all) to check whether all rotations of the number are prime.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0035/solution1.py):

```python
def is_circular_prime(n):
    return all(isprime(int(n[i:] + n[:i])) for i in range(len(n)))
```

The solution is then a simple sum of all numbers below one million that are circular primes.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0035/solution1.py):

```python
def circular_primes():
    return sum(is_circular_prime(str(i)) for i in range(2, 1000000))
```

