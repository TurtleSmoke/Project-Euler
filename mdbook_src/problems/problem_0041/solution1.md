# Brute force

Based on the definition of a pandigital number, we can deduce that it cannot contain more than 9 digits.
Therefore, we can iterate through every permutation of the digits in decreasing order until we find a prime number.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0041/solution1.py):

```python
def pandigital_prime():
    initial = "987654321"
    while True:
        for s in itertools.permutations(initial):
            n = int("".join(s))
            if isprime(n):
                return n
        initial = initial[1:]
```

Moreover, we can optimize the function slightly by taking into account that the sum of the digits in a 9-digit pandigital number is always 45, which makes it divisible by 3 and hence not prime.
The same applies to 8-digit pandigital numbers.
Therefore, we can skip these cases and start directly with 7-digit pandigital numbers.
However, the overall algorithm remains the same.