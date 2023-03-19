# Brute force

A straightforward approach to determine the smallest prime that belongs to an eight prime value family involves iterating through all primes and checking whether it is possible to replace \\( k \\) digits with numbers \\( d \\) ranging from \\( 0 \\) to \\( 9 \\) while still retaining 8 primes.
The condition being the difficulty of the problem, can be split into two parts:

- Find all the permutation of digits that should be replaced.
- Replace the digits with numbers ranging from \\( 0 \\) to \\( 9 \\) and check whether the resulting number is prime.

The first part can be done quite simply by generating a mask using [itertools.product](https://docs.python.org/3/library/itertools.html#itertools.product).
The mask is binary list with a length equal to the length of the number to verify, where the value `True` indicates that the digit at the same index should be replaced.

Although the second part may present some challenges in terms of efficiency, its implementation should remain straightforward since the method is intended to be naive.
To solve this, a string of the same length as the original number is constructed, where each digit is selected from either the initial number or the value \\( d \\), depending on the mask.

Certain corner cases requires some consideration:

- Number starting with \\( 0 \\) are invalid, otherwise the smallest seven prime value family would start at \\( 03 \\). Thus any permutation where the first digit is replaced by \\( 0 \\) should be skipped.
- The mask can not consist of only `False` values, as this would mean that no digit is replaced. Consequently, any permutations with an all-`False` mask should be discarded.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0051/solution1.py):

```python
def is_nth_prime_value_family(n):
    for mask in itertools.product([False, True], repeat=len(n)):
        seq_len = 0
        res = 0
        for d in "0123456789":
            if mask[0] and d == "0" or not any(mask):
                continue
            first = int("".join((d if mask[j] else n[j] for j in range(len(n)))))
            if isprime(first):
                if seq_len == 0:
                    res = first

                seq_len += 1
                if seq_len == 8:
                    return res
    return None
```


The remaining step simply iterate through all primes and verify whether the number is an eight prime value family.
For simplicity, the [sympy.sieve](https://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.generate.sieve) functions is used to generate an infinite sequence of primes.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0051/solution1.py):

```python
def prime_digit_replacements():
    for i in sieve:
        res = is_nth_prime_value_family(str(i))
        if res is not None:
            return res
```

