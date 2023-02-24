# Fewer loops is better

The [Brute force](./solution1.md) solution is too slow because it tries too many combinations.
We should try to reduce the number of possible combinations using the following observations:

- \\( 0 < a \leq b < c \\) because \\( a \\) and \\( b \\) are the shorter sides of the triangle. (1)
- \\( c = p - a - b \\) because \\( a + b + c \\) is the perimeter of the triangle. (2)

We can remove one loop thanks to (2), and reduces the number of possible combinations by half thanks to (1).
Furthermore, we do not need to check the condition \\( p = a + b + c \\) because we defined \\( c \\) using this equation.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution2.py):

```python
def count_pythagorean_triple(p):
    count = 0
    for a in range(1, p):
        for b in range(1, a):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count
```

Using the equations \\( a^2 + b^2 = c^2 \\) and \\( p = a + b + c \\) we can deduct the following:

- If both \\( a \\) and \\( b \\) are even, \\( c \\) will be even, thus \\( p \\) will be even.
- If both \\( a \\) and \\( b \\) are odd, \\( c \\) will be even, thus \\( p \\) will be even.
- If one is even and the other is odd, \\( c \\) will be odd, thus \\( p \\) will be even.

Therefore, we can reduce the number of possible combinations by only considering \\( p \\) that are even.
The solution to the problem is the maximum number of solutions for \\( p \\) below \\( 1000 \\).

The function will be the same as the last one, except that we will only iterate over even values of \\( p \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution2.py):

```python
def integer_right_triangles():
    return max(range(2, 1001, 2), key=count_pythagorean_triple)
```
