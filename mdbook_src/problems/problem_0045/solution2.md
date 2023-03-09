# Triangular numbers are useless

Let's start by observing the first ten Triangular, pentagonal, and hexagonal numbers:

- Triangular: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
- Pentagonal: 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
- Hexagonal: 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, ...

It appears that every Hexagonal number is also a Triangular number, specifically \\( H_n = T_{2n - 1} \\).
This relationship is true because \\( T_{2n - 1} = \frac{(2n - 1)(2n)}{2} = H_n \\).
Since every Hexagonal number is also a Triangular number, it's pointless to compute Triangular numbers.
Therefore, it is sufficient to iterate through every Hexagonal number and verify if it is also a Pentagonal number.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution2.py):

```python
def is_pentagonal(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()
```

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution2.py):

```python
def triangular_pentagonal_and_hexagonal():
    h = 145
    while not is_pentagonal(hn(h)):
        h += 1
    return hn(h)
```
