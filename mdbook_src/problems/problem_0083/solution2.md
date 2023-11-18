# Dijkstra's algorithm

## Problem

The problem is the exact same as [Problem 81](../problem_0081/problem.md) and [Problem 82](../problem_0082/problem.md), but this time, we can go everywhere.

## Grasping the solution

We can enhance our previous solution by using a more efficient algorithm.
The main drawback was the order in which we visited the nodes: none.
Instead, we could prioritize cells wth the lowest values, as they are more likely to be part of the shortest path.
This is exactly what [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) does.

## Implementation

The first step is to read the file and store the matrix, in this case, in a list of lists.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return [[int(x) for x in line.split(",")] for line in file.read().splitlines()]
```

The algorithm remains unchanged, but this time, we use a priority queue to store the nodes to be visited.
Given that we are visiting nodes in order, we can terminate the algorithm as soon as we reach the target node because we know that it will not be updated again.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/solution2.py):

```python
def dijkstra(matrix, source, target):
    updated = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    updated[0][0] = matrix[0][0]
    queue = [(updated[0][0], source)]

    while queue:
        _, (i, j) = hq.heappop(queue)
        if (i, j) == target:
            return updated

        for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                alt = updated[i][j] + matrix[x][y]
                if alt < updated[x][y]:
                    updated[x][y] = alt
                    hq.heappush(queue, (alt, (x, y)))

    return None
```

The last step is to return the value of the target node.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/solution2.py):

```python
def path_sum_four_ways(filename="matrix.txt"):
    matrix = read_file(filename)
    return dfs(matrix, (0, 0))[-1][-1]
```
