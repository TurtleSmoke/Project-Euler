# With a little thought

The [Brute force solution](solution1.md) can be simplified a bit knowing that
\\( a + b + c = 1000 \\) implies \\( c = 1000 - a - b \\). This removes a for
loop and an equation, since \\( a + b + c = 1000 \\) will always be true.

Another simplification can be made by knowing that \\( a < b < c \\). This
implies that \\( a \\), \\( b \\) and \\( c \\) are lower than 500, otherwise
\\( a + b + c \\) will be greater than 1000.

This gives us the following :

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution2.py):

```python
def special_pythagorean_triplet():
    for a in range(501):
        for b in range(a + 1, 501):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c

    return -1
```
