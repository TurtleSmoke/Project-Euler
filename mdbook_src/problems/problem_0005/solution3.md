# Least common multiple

Actually, the problem is to find
the [least common multiple](https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor)
which is:

\\[ LCT(1, 2, ..., N) \\]

To find the \\( LCT \\) of \\( 1 \\) through \\( N \\), we need all the primes
\\( \leqslant N \\). For each prime, we need its maximum power that won't exceed
\\( N \\). Which can be done easily using logarithms:

\\[ \begin{align} p^{k} &\leqslant N\\\\ k\log( p) &\leqslant \log( N)\\\\ k&=\left\lfloor \frac{\log( N)}{\log( p)}\right\rfloor\\\\ \end{align} \\]

So the \\( LCT \\) of \\( 1 \\) through \\( N \\) is:

\\[ \prod p^{\left\lfloor \frac{\log(N)}{\log(p)} \right\rfloor } \\]

We also know that it's pointless to search the maximum power of primes greater
than \\( \sqrt{n} \\) because it will always be 1.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0005/solution2.py):

```python
def smallest_multiple(n=20):
    # Returns a list of all primes <= n
    primes = sieve.primerange(n + 1)
    sqrt_n, log_n = sqrt(n), log(n)
    res = 1
    for p in primes:
        if p < sqrt_n:
            res *= p**(floor(log_n / log(p)))
        else:
            res *= p
    return res
```
