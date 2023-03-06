# Generation over iteration

Rather than iterating over all permutations and verifying the divisibility property like the [Brute force](./solution2.md) method, a more efficient solution is to recursively generate permutations that satisfy the divisibility property.

The process begins with all pandigital permutations with 3 digits that are divisible by \\( 2 \\).
Then we can generate all the permutations with 4 digits that are divisible by \\( 3 \\) by appending the new digits at the end of the previous permutations.
We can continue this process until all permutations with 10 digits are generated.

Since the first digit is not important in the divisibility property, it is simpler to start from the end of the number.
Thus, we begin with the permutations that are divisible by \\( 17 \\) and continue adding the remaining digits at the beginning of the previous permutations.

Because the final number cannot start with \\( 0 \\), we can disregard the permutations that start with \\( 0 \\) in the final concatenation.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0043/solution2.py):

```python
def sub_string_divisibility():
    digits = "0123456789"
    items = [x + y for x in digits for y in digits if x != y]  # Permutations of 2 digits

    for d in [17, 13, 11, 7, 5, 3, 2]:
        items = [
            y + x for x in items for y in digits if int((y + x)[:3]) % d == 0 and y not in x
        ]  # Concatenation at the beginning

    items = [int(y + x) for x in items for y in digits[1:] if y not in x]  # Last concatenation

    return sum(items)
```
