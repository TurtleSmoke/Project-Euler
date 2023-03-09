# Diophantine equations

The [Triangular numbers are useless](./solution2.md) approach exploits the fact that Triangular numbers are useless.
Thus, it is sufficient to find \\( H_n = T_n \Leftrightarrow 3n^2 - n + 4m^2 - 4m = 0 \\).
This is known as a [Diophantine equation](https://en.wikipedia.org/wiki/Diophantine_equation).
This problem is very hard to solve in general, so we will use this [solver](https://www.alpertron.com.ar/QUAD.HTM) to find the solution.

It gives the following recurrence relation:

\\[ 
x_{n + 1} = 97x_n + 112y_n - 44\\\\
y_{n + 1} = 84x_n + 97y_n - 38
\\]

Starting with the solution \\( (n, m) = (1, 1) \\), we can easily find the third solution.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution3.py):

```python
def triangular_pentagonal_and_hexagonal():
    x_n = lambda x_i, y_i: 97 * x_i + 112 * y_i - 44
    y_n = lambda x_i, y_i: 84 * x_i + 97 * y_i - 38

    x, y = 1, 1
    x, y = x_n(x, y), y_n(x, y)
    y = y_n(x, y)
    return y * (2 * y - 1)
```
