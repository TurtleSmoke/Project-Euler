import numpy as np

# Read file saved by solution1.py
matrix = np.genfromtxt("matrix.csv", delimiter=",", dtype=np.float64)
transitions = np.genfromtxt("transitions.csv", delimiter=",", dtype=np.float64)

# Check difference between the two matrices
for i in range(120):
    if not np.isclose(matrix[i, :], transitions[i, :]).all():
        for j in range(120):
            if not np.isclose(matrix[i, j], transitions[i, j]):
                print(i, j, matrix[i, j], transitions[i, j])

dice = np.array([
    [0, 0.5, 0.5],
    [0.5, 0, 0.5],
    [0.8, 0.2, 0],
])

expected = np.array([
    [0, 0.3, 0.7],
    [0.5, 0, 0.5],
    [0.8, 0.1, 0.1],
])
card = [(1, 1, 0.5), (1, 2, 0.5)]
cards = np.array([
    [1, 0, 0],
    [0, 0.5, 0.5],
    [0, 0, 1],
])

print(dice @ cards)
