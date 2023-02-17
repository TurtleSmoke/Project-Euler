import numpy as np


def number_spiral_diagonals(n=1001):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # EAST, SOUTH, WEST, NORTH
    cur_dir = 0
    (x, y) = (n // 2, n // 2)  # Center of the matrix
    spiral = np.zeros(n * n, dtype=int).reshape(n, n)
    spiral[x, y] = 1

    for i in range(2, n * n + 1):
        # Move along the current direction and update the new cell
        dx, dy = dirs[cur_dir]
        x, y = x + dx, y + dy
        spiral[x, y] = i

        # If the cell in the next direction is empty: change direction
        dx, dy = dirs[(cur_dir + 1) % 4]
        if spiral[x + dx, y + dy] == 0:
            cur_dir = (cur_dir + 1) % 4

    return np.trace(spiral) + np.trace(np.fliplr(spiral)) - 1


if __name__ == "__main__":
    print(number_spiral_diagonals())
