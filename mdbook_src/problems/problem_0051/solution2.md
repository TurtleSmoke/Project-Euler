# Simple observations

The [Brute force](./solution1.md) approach is very slow and highly inefficient, mainly due to redundant verification.
For example, several numbers, such as \\( 12345 \\) and \\( 12346 \\), are checked multiples times when the replacement includes the last digit.
Therefore, it is necessary to find a better approach to determine which numbers and which replacements are required.

Let's start with some simple observations that can be made to improve the efficiency of the algorithm:

1. Since the first number of the sequence must be a prime, there is no need to check numbers lower than the current one during digit replacement.
   This is because smaller prime are already been verified.
2. Since the family is an eight prime value family, at least 8 replacements must be prime.
   Using **1**, it's unnecessary to replace digits greater than \\( 2 \\), as this would result in fewer than 8 possible replacements.
3. Only replacements of \\( 3k \\) digits, with \\( k > 0 \\) can give a solution.
   Let's first remember that a number \\( n \\) is divisible by \\( 3 \\) if and only if the sum of its digits is divisible by \\( 3 \\).
   The rest modulo \\( 3 \\) of the sum of the digits of the initial numbers excluding the one that will be replaced is either \\( 0 \\), \\( 1 \\) or \\( 2 \\).
   If the number of replacements is \\( 2 \\), then the rest modulo \\( 3 \\) of the sum of the replacements for \\( 0 \\) to \\( 9 \\) is: \\( 0 \\), \\( 2 \\), \\( 1 \\), \\( 0 \\), \\( 2 \\), \\( 1 \\), \\( 0 \\), \\( 2 \\), \\( 1 \\), \\( 0 \\) respectively.
   Therefore, whatever the initial number is, the sum of the digits will always be divisible by \\( 3 \\) at least 3 times, and thus the maximum value family is \\( 7 \\).
   The same reasoning can be applied to other non-multiples of \\( 3 \\) digits replacements.
4. Using **1**, it is possible to generate the replacements more efficiently by adding to the current number the mask multiplied by the nth digit.
   For example, if the current number is \\( 12345 \\) and the mask is \\( 00101 \\), then the replacement is \\( 12345 + 101 * d \\).

Using these observations, it is possible to compute much more efficiently the prime digit replacements.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0051/solution2.py):

```python
def is_nth_prime_value_family(n):
    for d in range(3):  # Observation 2
        mask = 0
        occurrences = 0
        for i, m in enumerate(str(n)[::-1]):  # Reverse string for easier mask creation
            if m == str(d):
                mask += 10**i
                occurrences += 1

        if occurrences == 0 or occurrences % 3 != 0:  # Observation 3
            continue

        seq_len = 0
        for r in range(10 - d):
            if seq_len + 10 - r < 8:  # Observation 2
                break
            if isprime(n + r * mask):  # Observation 4
                seq_len += 1
            if seq_len == 8:
                return n
```

The remaining step is the same as the [Brute force](./solution1.md) approach.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0051/solution2.py):

```python
def prime_digit_replacements():
    for i in sieve:
        res = is_nth_prime_value_family(i)
        if res is not None:
            return res
```
