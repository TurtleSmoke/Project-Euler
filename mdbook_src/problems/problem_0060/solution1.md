# Brute force

The problem requires finding the set of five primes that has the lowest sum and for which any two primes concatenate to produce another prime.
A brute force approach can be used, but it requires to generate all the primes up to a certain arbitrary limit.
Then, 5 nested loops are used to find the first set of five primes that satisfy the condition.
If the concatenation of two primes is not prime, the search for the current set of primes can be stopped.

Determining whether two concatenated primes are prime is done by converting the numbers to strings and checking whether the concatenation of the strings is prime.
It is worth noting that another method involving logarithms can be used to determine whether the concatenation of two numbers is prime, but it is not as straightforward as the string approach.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0060/solution1.py):

```python
def concat(p1, p2):
    return isprime(int(str(p1) + str(p2))) and isprime(int(str(p2) + str(p1)))
```

The rest is the 5 nested loops, for each loop, only the new prime is checked against the previous ones.
The limit is set to 10000, which is enough to find the solution.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0060/solution1.py):

```python
def prime_pair_sets():
    primes = list(sieve.primerange(10000))
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes[:i]):
            if any(not concat(p, p2) for p in (p1,)):
                continue
            for k, p3 in enumerate(primes[:j]):
                if any(not concat(p, p3) for p in (p1, p2)):
                    continue
                for l, p4 in enumerate(primes[:k]):
                    if any(not concat(p, p4) for p in (p1, p2, p3)):
                        continue
                    for p5 in primes[:l]:
                        if all(concat(p, p5) for p in (p1, p2, p3, p4)):
                            return p1 + p2 + p3 + p4 + p5
```

This solution may not yield the smallest sum because the order of iteration is not designed to minimize the sum.