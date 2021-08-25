# Brute force

We are searching for \\( a \\), \\( b \\) and \\( c \\) such that \\( a < b
< c \\), \\( a + b + c = 1000 \\) and \\( a^2 + b^2 = c^2 \\). The brute force
solution will simply iterate to 1000 for \\( a \\), \\( b \\)
and \\( c \\) and stop when the above equations are true.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution1.py):

```python
def special_pythagorean_triplet():
    for a in range(1001):
        for b in range(a + 1, 1001):
            for c in range(b + 1, 1001):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a * b * c
               
    return -1
```
