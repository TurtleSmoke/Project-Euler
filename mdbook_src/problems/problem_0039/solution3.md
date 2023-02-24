# Even fewer loops

The [Fewer loops is better](./solution2.md) solution is still very slow.
However, we can make the solution faster by using the equations \\( c = p - a - b \\) and \\( a^2 + b^2 = c^2 \\) together.

We can rewrite \\( a^2 + b^2 = c^2 \\) as \\( a^2 + b^2 = (p - a - b)^2 \\) and simplify it to \\( 2b(p - a) = p(p - 2a) \\).

Using this equation, we have \\( b = \frac{p(p - 2a)}{2(p - a)} \\).
We can use this information to remove the loop for \\( b \\).

Furthermore, \\( b \\) must be a positive integer and since \\( 2(p - a) \\) is always positive, \\( p - 2a \\) must be positive as well.
It implies that \\( a < 500 \\).

Finally, we can iterate over all values of \\( a \\) less than \\( 500 \\), and check whether \\( p(p - 2a) \\) is divisible by \\( 2(p - a) \\).
Summing the number of solutions will give us the number of pythagorean triples for a given \\( p \\).

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution3.py):

```python
def count_pythagorean_triple(p):
    return sum(p * (p - 2 * a) % (2 * (p - a)) == 0 for a in range(1, p // 2))
```

The rest is the same as the previous solution.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0039/solution3.py):

```python
def integer_right_triangles():
    return max(range(2, 1001, 2), key=count_pythagorean_triple)
```
