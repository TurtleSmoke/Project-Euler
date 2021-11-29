# Brute force

This problem actually contains two problem. The first is the spiral creation
problem and the second is the diagonal sum problem.

The direction of the spiral is a cycle of 'EAST', 'SOUTH', 'WEST' and 'NORTH'
but the main question is to know when it changes.

There is many ways of creating a spiral matrix, but the idea I had was to insert
number in every cell in the same direction until the cell in the next direction
is empty.

Once the spiral matrix is created, we can compute the diagonal using the
`trace` function of numpy. We also need to remove the cell in the middle because
it will be counted twice.

```python
def number_spiral_diagonals(n=1001):
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # EAST, SOUTH, WEST, NORTH
    cur_dir = 0
    (x, y) = (n // 2, n // 2)  # Center of the matrix
    spiral = np.zeros(n * n, dtype=int).reshape(n, n)
    spiral[x, y] = 1

    for i in range(2, n * n + 1):
        # Move along the current direction and update the new cell
        dx, dy = dir[cur_dir]
        x, y = x + dx, y + dy
        spiral[x, y] = i

        # If the cell in the next direction is empty: change direction
        dx, dy = dir[(cur_dir + 1) % 4]
        if spiral[x + dx, y + dy] == 0:
            cur_dir = (cur_dir + 1) % 4

    return np.trace(spiral) + np.trace(np.fliplr(spiral)) - 1
```
