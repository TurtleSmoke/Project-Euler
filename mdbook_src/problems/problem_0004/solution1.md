# Brute force

We are searching the largest palindrome made from the product of two 3-digit
numbers. Firstly, it is necessary to know when a number is a palindrome. This
can be done easily using python iteration.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0004/solution1.py):

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]
```

A better solution exists using modulus and division, but performance is not the
goal here.

The range of 3-digit numbers is \\( [100; 999] \\), the naive solution will
consist in simply iterate over each number and check which product is the
largest palindrome. A little trick: if \\( 100 * 200 \\) does not work, \\(
200 * 100 \\) won't work either, so the second loop starts from the current
number of the first one.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0004/solution1.py):

```python
def largest_palindrome_product():
    res = 0
    for x in range(100, 1000):
        for y in range(x, 1000):
            if x * y > res and is_palindrome(x * y):
                res = x * y
                
    return res
```
