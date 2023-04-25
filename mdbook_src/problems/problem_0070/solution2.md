# Euler's totient function

Recalling that \\( \phi(n) = n(1 - \frac{1}{p_1})(1 - \frac{1}{p_2})\dots(1-\frac{1}{p_k}) \\) with \\( n = p_1^{e_1}p_2^{e_2}\dots p_k^{e_k} \\).
It is obvious that minimizing \\( \frac{n}{\phi(n)} \\) is equivalent to maximizing \\( \phi(n) \\).

To maximize \\( \phi(n) \\), it is ideal to choose \\( n \\) with as few prime factors as possible.
Ideally, \\( n \\) should be a prime number, but it does not result with a permutation as \\( \phi(n) = n - 1 \\).
Additionally, \\( n \\) can not be equal to \\( p^k \\) as \\( n=p^k \\) and \\( \phi(n) = p^{k-1}(p-1) \\) are not permutations of each other.
This can be proven by working modulo 3, but since the proof is not relevant, it is assumed to be true.

Hence, a product of two primes should be chosen, where the two primes are as large as possible, close to each other, and to \\( \sqrt{10^7} \\).
If no such prime pair exists, then a product of three primes should be chosen, and so on.

If \\( a \\) and \\( b \\) are permutations of each other, then \\( a - b \\) is a multiple of \\( 9 \\).
Therefore, if \\( n \\) is a permutation of \\( \phi(n) \\), then \\( n - \phi(n) = p_1 + p_2 -1 \\) must be a multiple of \\( 9 \\).
This property can be used to filter out totients that are not permutations of their index without having to compute the full check, which is computationally expensive.

To find the solution, it is sufficient to consider \\( n \\) as a product of two primes, so the code below does not consider products of more than two primes.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0070/solution2.py):

```python
def totient_permutation(limit=10000001):
    primes = list(sieve.primerange(2, 2 * int(limit**0.5)))
    res = 0
    ratio = float("inf")
    for i in range(len(primes)):
        for j in range(i):
            if (primes[i] + primes[j] - 1) % 9 != 0:
                continue
            n = primes[i] * primes[j]
            if n > limit:
                break
            t = (primes[i] - 1) * (primes[j] - 1)
            if n / t < ratio and sorted(str(n)) == sorted(str(t)):
                res = n
                ratio = n / t
    return res
```

While the most optimal iteration would involve iterating over all primes sorted by their distance to \\( \sqrt{10^7} \\), it is a more complex approach to implement and not worth the effort.
Therefore, for simplicity, the primes are iterated over in ascending order, and the limit is arbitrarily set to \\( 2\sqrt{10^7} \\).