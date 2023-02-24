# Brute force

The problem actually requires us to find [Pythagorean triples](https://en.wikipedia.org/wiki/Pythagorean_triple) with a perimeter of \\( p \\) less than \\( 1000 \\).
To find the solution for this problem, we can try every possible combination of values for \\( \\{a,b,c\\} \\) for every \\( p \\) and check if \\( p = a + b + c \\) and \\( a^2 + b^2 = c^2 \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution1.py):

```python
def count_pythagorean_triple(p):
    count = 0
    for a in range(1, p):
        for b in range(1, p):
            for c in range(1, p):
                if a + b + c == p and a * a + b * b == c * c:
                    count += 1
    return count
```

We want to find the maximum value returned by `count_right_triangles` but return the \\( p \\) that corresponds to that value.
We can use the Python [max](https://docs.python.org/3/library/functions.html#max) builtin with key equal to our function to get the \\( p \\) that corresponds to the maximum value returned by `count_right_triangles`.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution1.py):

```python
def integer_right_triangles():
    return max(range(1, 1001), key=count_pythagorean_triple)
```
