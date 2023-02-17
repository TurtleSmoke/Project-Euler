# Dynamic programming

The [Summation minus summation](solution2.md) solution gives an interesting
solution because we found the sum of the primes less than \\( n \\) with only
the primes less than \\( \sqrt{n} \\). Unfortunately, this solution is not
efficient because it requires too much recursion for larger n.

The main problem with the previous solution was to remove the numbers that were
multiples of previous primes. For example with the multiples of \\( 3 \\), the
number \\( 6 \\) was already removed by the multiples of \\( 2 \\).

What we really want is to remove the multiples of \\( 3 \\) that have not
already been removed by the multiples of \\( 2 \\) such as \\( 6 \\), \\( 12 \\)
... For \\( 5 \\) that would be the number that are neither multiples of \\( 2
\\) nor \\( 3 \\).

Instead of the sum of the multiples of a prime, we will search for the sum of
integer that remain after sieving with all primes smaller than the current one.

This solution is well explained by **Lucy_Hedgehog** in this
[thread](https://projecteuler.net/thread=10;page=5#111677) (only available if
you solve the problem):

> The main idea is as follows: Let \\( S(v,m) \\) be the sum of integers in the
> range \\( 2 \dots v \\) that remain after sieving with all primes smaller or
> equal than \\( m \\). That is \\( S(v,m) \\) is the sum of integers up to
> \\( v \\) that are either prime or the product of primes larger than \\( m
> \\).
>
> \\( S(v, p) \\) is equal to \\(S(v, p-1) \\) if \\( p \\) is not prime or
> \\( v \\) is smaller than \\( p\*p \\). Otherwise (\\( p \\) prime, \\(
> p\*p\leqslant v \\)) \\( S(v,p) \\) can be computed from \\(S(v, p-1)\\)
> by finding the sum of integers that are removed while sieving with \\( p
> \\). An integer is removed in this step if it is the product of \\(p \\)
> with another integer that has no divisor smaller than \\(p \\). This can
> be expressed as
>
> \\[ S\left(v, p \right) = S\left(v, p - 1\right) - p\left(S\left(\frac{v}{p},
> p - 1\right) -S\left(p-1, p-1\right)\right) \\]
>
> Dynamic programming can be used to implement this. It is sufficient to
> compute \\( S(v,p) \\) for all positive integers \\( v \\) that are
> representable as \\( \left\lfloor\frac{n}{k}\right\rfloor \\) for some
> integer \\( k \\) and all.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0010/solution3.py):

```python
def partial_prime_sum(n=2000000):
    r = ceil(sqrt(n))
    V = [n // i for i in range(1, r + 1)]
    V += list(range(V[-1] - 1, 0, -1))
    S = {i: i * (i + 1) // 2 - 1 for i in V}
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:  # p is prime
            sp = S[p - 1]  # sum of primes smaller than p
            p2 = p * p
            for v in V:
                if v < p2:
                    break
                S[v] -= p * (S[v // p] - sp)
    return S[n]
```
