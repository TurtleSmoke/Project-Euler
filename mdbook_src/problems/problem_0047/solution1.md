# Brute force

To find the first four consecutive integers that possess four distinct prime factors each using a brute force approach can be separated into two steps:

- Find the prime decomposition of a number.
- Iterate over all numbers and check if the next four numbers have four distinct prime factors each.

The prime decomposition has previously been implemented in other problems and, therefore, is not an important component for this approach.
To solve this part, the [sympy.primefactors](https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.factor_.primefactors) function can be used.

The iteration process is straightforward, and the number of distinct primes can be determined using the length of the set of the prime decomposition.
To identify the solution, check the next four numbers that have four distinct prime factors each, and return the first number that satisfies this condition.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0047/solution1.py):

```python
def distinct_primes_factors():
    for i in itertools.count(5):
        if (
            len(set(primefactors(i)))
            == len(set(primefactors(i + 1)))
            == len(set(primefactors(i + 2)))
            == len(set(primefactors(i + 3)))
            == 4
        ):
            return i
```
