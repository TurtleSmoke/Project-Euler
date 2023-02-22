# Brute force

Detecting palindromes with Python's string slicing is easy.
We can use the same approach to detect palindromes in binary form.
Python's [bin](https://docs.python.org/3/library/functions.html#bin) function returns the binary representation of an integer with a `0b` prefix.
If you remove this prefix, we can use the same function to check if the number is a palindrome in binary form.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0036/solution1.py):

```python
def is_double_palindrome(n):
    is_palindrome = lambda s: s == s[::-1]
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])
```

To find the solution, we can sum all the number below 1 million that are palindromes in both decimal and binary form. 

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0036/solution1.py):

```python
def double_base_palindromes():
    return sum(n for n in range(1000000) if is_double_palindrome(n))
```
