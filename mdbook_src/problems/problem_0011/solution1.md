# Brute force

This problem is not interesting, the solution is simply to iterate on each 
row, column and on the two diagonal.

As with [Largest product in a series](../problem_0008/problem.md), the 
input grid will be stored in a file, so the first step is to obtain this
grid as int matrix.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0011/read_file.py):

```python
def read_file(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in line.split(' ')] for line in
                file.read().split('\n')[:-1]]  # Last element is an empty line
```

And then just iterate on this matrix:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0011/solution1.py):

```python
def largest_product_in_grid(filename):
    g = read_file(filename)

    for y in range(0, 20):
        for x in range(0, 17):
            yield g[x][y] * g[x + 1][y] * g[x + 2][y] * g[x + 3][y]
    for x in range(0, 20):
        for y in range(0, 17):
            yield g[x][y] * g[x][y + 1] * g[x][y + 2] * g[x][y + 3]
    for y in range(0, 17):
        for x in range(0, 17):
            yield g[x][y] * g[x + 1][y + 1] * g[x + 2][y + 2] * g[x + 3][y + 3]
    for x in range(3, 20):
        for y in range(0, 17):
            yield g[x][y] * g[x - 1][y + 1] * g[x - 2][y + 2] * g[x - 3][y + 3]
```
