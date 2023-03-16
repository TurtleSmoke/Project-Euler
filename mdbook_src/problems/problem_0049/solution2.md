# Primes permutations

An improvement to the [Brute force](./solution1.md) approach can be made by avoiding the iterations over all numbers.
The most restrictive requirements of the problem are that the solution must be four-digit and prime.
Fortunately, meeting this condition is really simple as generating the Sieve of Eratosthenes between \\( 1000 \\) and \\( 10000 \\) gives a list of all four-digit primes.

The remaining conditions require that the three numbers must be permutations of each other and in arithmetic progression.
However, it's difficult to determine all primes that are in arithmetic progression efficiently.
As a result, it is better to focus on the permutation requirement.
By grouping all primes based on their sorted digits results in lists of four-digit primes with the same permutations.

Finally, the arithmetic constraint can be verified by iterating through each group to find \\( p_1 \\), \\( p_2 \\), and \\( p_3 \\) such that \\( p_3 = 2p_2 - p_1 \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0049/solution2.py):

```python
def prime_permutations():
    primes = list(sieve.primerange(1000, 10000))
    primes_permutations = defaultdict(list)
    for prime in primes:
        primes_permutations["".join(sorted(str(prime)))].append(prime)

    for perm in primes_permutations.values():
        if len(perm) < 3 or perm[0] == 1487:
            continue

        for i, p1 in enumerate(perm):
            for p2 in perm[i + 1 :]:
                p3 = 2 * p2 - p1
                if p3 in perm:
                    return str(p1) + str(p2) + str(p3)
```
