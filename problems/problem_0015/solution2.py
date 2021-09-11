import numpy as np


def lattice_paths(n=20):
    n += 1
    paths = np.zeros((n, n), dtype=int)

    for i in range(1, n):
        paths[i, 0] = 1
        paths[0, i] = 1

    for i in range(1, n):
        for j in range(1, n):
            paths[i, j] = paths[i - 1, j] + paths[i, j - 1]

    return paths[n - 1, n - 1]


if __name__ == "__main__":
    print(lattice_paths())
