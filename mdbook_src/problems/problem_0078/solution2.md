# Euler partition function

The [partition function](https://en.wikipedia.org/wiki/Partition_function_(number_theory)) \\( p(n) \\) represents the number of ways to partition \\( n \\) coins into piles of size \\( k \\) or less, that is, the function we are looking for.
Using [Euler's recurrence relation](https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations), we can calculate \\( p(n) \\) for any \\( n \\):
\\[
\begin{aligned}
    p(n) &= \sum_{k\in\mathbb{Z}\backslash\\{0\\}}^{\infty} (-1)^{k+1} p \left( n - \frac{k(3k-1)}{2} \right)\\\\
         &= \sum_{k=1}^{\infty} (-1)^{k+1} \left[ p \left( n - \frac{k(3k-1)}{2} \right) + p \left( n - \frac{k(3k+1)}{2} \right) \right]
\end{aligned}
\\]

This summation is over all nonzero integers \\( k \\), but since \\( p(n) = 0 \\) for \\( n < 0 \\), the series has only finitely many nonzero terms, and can be computed in a finite amount of time.

Using python mutable variables as a cache for previously computed \\( p(n) \\) values, we can compute \\( p(n) \\) much more effeciently than the last solution.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0078/solution2.py):

```python
def p(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 0:
        return 0
    if n < 2:
        return 1

    cum_sum = 0
    for k in range(1, n + 1):
        n1 = n - k * (3 * k - 1) // 2
        n2 = n - k * (3 * k + 1) // 2
        cum_sum += (-1) ** (k + 1) * (p(n1, cache) + p(n2, cache))
        if n1 <= 0:  # n1 < n2, no need to check both
            break

    cache[n] = cum_sum % 1000000
    return cache[n]
```

The rest is to find the smallest \\( n \\) such that \\( p(n) \\) is divisible by \\( 10^6 \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0078/solution2.py):

```python
def coin_partitions(n=1000000):
    for i in itertools.count(0):
        r = p(i)
        if r % n == 0:
            return i
```
