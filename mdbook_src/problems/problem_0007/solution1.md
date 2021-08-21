# Brute force

A well known and fast way to generate primes is the
[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
The only problem is that we need an upper bound, which is not the case here
since we don't know the size of the 10001st prime.

We will have to test the primality of each number, if it is prime, then we store
it, otherwise we continue with the next number until the list of prime numbers
that we stored contains 10001 elements. The last one being the answer.

To determine the primality of a number, we can check if one of the preceding
primes can divide it, if not, the number is prime.

Since even number can not be prime, we can go two by two just like
the [Two by Two](../problem_0003/solution2.md) solution
of [Problem 3: Largest prime factor](../problem_0003/problem.md).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0007/solution1.py):

```python
def n_th_prime(n=10001):
    i = 3
    primes = [2]
    while len(primes) < n:
        if all(i % p != 0 for p in primes):  # No divisor in the previous prime.
            primes.append(i)
        i += 2

    return primes[-1]
```
