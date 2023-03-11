# Good old Sieve

The [Cache is life](./solution2.md) approach involves computing the prime decomposition of each number, which is a costly operation that can be avoided using a sieve.
The downside of this approach is that the sieve requires an arbitrary limit, but it can be increased until the solution is found.
Instead of determining which number are primes, the sieve stores the number of distinct prime factors for each number.

The [sympy.primefactors](https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.primefactors) function combined multiples algorithm, making its exact complexity difficult to determine.
Nevertheless, it is expected to be no more than \\( O(sqrt{n}) \\), resulting in a previous approach of \\( O(n\sqrt{n}) \\).

The Sieve of Eratosthenes complexity is \\( O(n\log\log{n}) \\), which is better than the previous approach.
In practive, \\( \log\log{n} \\) is very small and can be disregarded for simplicity, resulting in a complexity of \\( O(n) \\).

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0047/solution3.py):

```python
def factors_sieves(n):
    factors = [0] * (n + 1)
    consecutive = 0
    for i in range(2, n + 1):
        if factors[i] == 0:
            for j in range(2, int(n / i)):
                factors[i * j] += 1
            consecutive = 0
        elif factors[i] == 4:
            consecutive += 1
        else:
            consecutive = 0

        if consecutive == 4:
            return i - 3
    return None
```

To find the final solution, one can arbitrarily choose a limit and attempt to find a solution.
If no solution is found, the limit can be multiplied by two, and the process can be repeated.
The complexity of this operation is \\( O(1 + 2 + 4 + 8 ... + n) \\) which is equal to \\( O(2n) \\) and equivalent to \\( O(n) \\).

In theory, this approach should be faster than the previous one, but in practice, it may not be faster for small limits.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0047/solution3.py):

```python
def distinct_primes_factors():
    for i in itertools.count(1):
        res = factors_sieves(2**i)
        if res is not None:
            return res
```
