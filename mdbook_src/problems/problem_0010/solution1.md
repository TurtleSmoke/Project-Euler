# Brute force

We already know, thanks to te previous problems that when one search for all
prime numbers below a certain limit, the sieve of eratosthenes is a good
solution.

It is enough to sum the list of the primes found with the sieve.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0010/solution1.py):

```python
def summation_of_primes(limit=2000000):
    return sum(sieve.primerange(limit))
```
