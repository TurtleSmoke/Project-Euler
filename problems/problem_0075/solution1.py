import numpy as np
from collections import defaultdict

A = np.array(
    [
        [1, -2, 2],
        [2, -1, 2],
        [2, -2, 3],
    ]
)

B = np.array(
    [
        [1, 2, 2],
        [2, 1, 2],
        [2, 2, 3],
    ]
)

C = np.array(
    [
        [-1, 2, 2],
        [-2, 1, 2],
        [-2, 2, 3],
    ]
)


def compute_all_pythagorean_triples(results, max_p, abc):
    curr_p = sum(abc)
    if curr_p < max_p:
        for perimeter in range(curr_p, max_p, curr_p):
            results[perimeter] += 1
        compute_all_pythagorean_triples(results, max_p, A @ abc)
        compute_all_pythagorean_triples(results, max_p, B @ abc)
        compute_all_pythagorean_triples(results, max_p, C @ abc)


def singular_integer_right_triangles():
    results = defaultdict(int)
    compute_all_pythagorean_triples(results, 1500000, np.array([3, 4, 5]))
    return sum(filter(lambda x: x == 1, results.values()))


if __name__ == "__main__":
    print(singular_integer_right_triangles())
