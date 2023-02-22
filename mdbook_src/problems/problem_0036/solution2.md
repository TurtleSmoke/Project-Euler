# Generating palindromes

The [Brute force](./solution1.md) solution iterates over all numbers and check if they are palindromes.
We can directly generate palindromes in decimal form and then check if they are palindromic in binary form.

Palindrome are of the form:

- `abccba`
- `abcba`
- `abba`
- `aba`
- `aa`
- `a`

To generate these, we can create the left half of the palindrome and then mirror it to get the full palindrome.
We just have to be careful with the even and odd cases, like `abba` and `aba`.

Because the palindromes limit is 1 million, the left part must be smaller than 1000.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0036/solution2.py):

```python
def make_palindrome():
    left = 1
    while left < 1000:
        yield int(str(left) + str(left)[::-1][1:])  # Odd length palindromes
        yield int(str(left) + str(left)[::-1])  # Even length palindromes
        left += 1
```

The final solution just need to check palindromes in their binary form.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0036/solution2.py):

```python
def double_base_palindromes():
    return sum(n for n in make_palindrome() if is_bin_palindrome(n))
```
