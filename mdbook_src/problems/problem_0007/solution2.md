# Almost six by six

Actually, it is possible to speed up a little the previous program knowing that
every prime \\( n > 3 \\) is of the form :

\\[ 6k+1 \text{ or } 6k-1 \\]

Let's try to persuade ourselves that this is true. All prime numbers are of the
form:

\\[ 6k - 1\\\\ 6k\\\\ 6k+1\\\\ 6k+2\\\\ 6k+3\\\\ 6k+4\\\\ \\]

Nothing amazing, but as we are looking for prime number, we can remove some of
them :

\\( 6k \\), \\( 6k + 2 \\) and \\( 6k + 4 \\) are even number, so they cannot be
prime.

\\( 6k + 3 = 3(3k + 1) \\) which is divisible by 3 and thus not prime
(except 3).

Which let us with: \\( 6k + 1 \\) and \\( 6k - 1 \\).

Thus, we can rewrite the old program to check only those numbers.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0007/solution2.py):

```python
def n_th_prime(n=10001):
    i = 1
    primes = [2, 3]
    while len(primes) < n:
        if all((6 * i - 1) % p != 0 for p in primes):
            primes.append(6 * i - 1)
        if all((6 * i + 1) % p != 0 for p in primes):
            primes.append(6 * i + 1)
        i += 1

    return primes[n - 1]
```
