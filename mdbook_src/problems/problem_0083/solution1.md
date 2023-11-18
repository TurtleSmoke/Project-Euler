# Breadth-first search

## Problem

The problem is the exact same as [Problem 81](../problem_0081/problem.md) and [Problem 82](../problem_0082/problem.md), but this time, we can go everywhere.

## Grasping the solution

Because of this freedom of movement, we can not use the same approach as before, so let's explore other options.
If we try to solve this problem with pen and paper, we would start from the top left corner, updating cells one by one just as follows:

In this example, green cells are currently being updated, red ones have been updated, and blue cells, while updated previously, are being updated again.

\\[
\begin{align}
&\begin{pmatrix}
\color{green}{131} & 673 & 234 & 103 & 18\\\\
201 & 96 & 342 & 965 & 150\\\\
630 & 803 & 746 & 422 & 111\\\\
537 & 699 & 497 & 121 & 956\\\\
805 & 732 & 524 & 37 & 331\\\\
\end{pmatrix}
\rightarrow
\begin{pmatrix}
\color{red}{131} & \color{green}{804} & 234 & 103 & 18\\\\
\color{green}{332} & 96 & 342 & 965 & 150\\\\
630 & 803 & 746 & 422 & 111\\\\
537 & 699 & 497 & 121 & 956\\\\
805 & 732 & 524 & 37 & 331\\\\
\end{pmatrix}
\rightarrow\\\\
&\begin{pmatrix}
\color{red}{131} & \color{red}{804} & \color{green}{1035} & 103 & 18\\\\
\color{red}{332} & \color{green}{428} & 342 & 965 & 150\\\\
\color{green}{962} & 803 & 746 & 422 & 111\\\\
537 & 699 & 497 & 121 & 956\\\\
805 & 732 & 524 & 37 & 331\\\\
\end{pmatrix}
\rightarrow
\begin{pmatrix}
\color{red}{131} & \color{red}{804} & \color{red}{1035} & \color{green}{1138} & 18\\\\
\color{red}{332} & \color{red}{428} & \color{green}{770} & 965 & 150\\\\
\color{red}{962} & \color{green}{1231} & 746 & 422 & 111\\\\
\color{green}{1499} & 699 & 497 & 121 & 956\\\\
805 & 732 & 524 & 37 & 331\\\\
\end{pmatrix}
\rightarrow\\\\
&\begin{pmatrix}
\color{red}{131} & \color{red}{804} & \color{blue}{1004} & \color{red}{1138} & \color{green}{1156}\\\\
\color{red}{332} & \color{red}{428} & \color{red}{770} & \color{green}{1735} & 150\\\\
\color{red}{962} & \color{red}{1231} & \color{green}{1516} & 422 & 111\\\\
\color{red}{1499} & \color{green}{1930} & 497 & 121 & 956\\\\
\color{green}{2304} & 732 & 524 & 37 & 331\\\\
\end{pmatrix}
\rightarrow \dots
\end{align}
\\]

Notice that the blue cell is udpated twice.
If we were solving this by hand, we would update its neighbors once more.
Continuing this process leads us to the bottom right corner.
Basically, its like a [breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) but with a twist: if a cell is being updated again, we revisit its neighbors (unlike traditional BFS, where nodes are not revisited).
Moreover, we know that there will not be any cycles, so we can terminate the algorithm in a finite number of steps.

## Implementation

The first step is to read the file and store the matrix, in this case, in a list of lists.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return [[int(x) for x in line.split(",")] for line in file.read().splitlines()]
```

When updating the blue cell in the example, we compared the updated value of the blue cell \\( (1035) \\) with the initial value of the blue cell \\( (234) \\) plus the updated value of its neighbor \\( (770) \\).
To implement this, we need to know both the initial value and the updated value of each cell.
A straightforward solution is to create a copy of the matrix where each cell is initialized with the maximum value, indicating that it hasn't been updated it yet.

We have two matrixes: the initial matrix \\( I \\) and the updated matrix \\( U \\).
For each cell \\( (i, j) \\), we update its neighbor \\( (ni, nj) \\) to the minimum between its current value and the sum of the current cell \\( (i, j) \\) in the updated matrix and the the neighbor cell \\( (ni, nj) \\) in the initial matrix:
\\[
U(ni, nj) = \min \left( U(ni, nj), U(i, j) + I(ni, nj) \right )
\\]
As the updated matrix is initialized with the maximum value, it ensures that non-updated neighbors will always have values greater than other paths.
Every time a neighbor is updated, we add it to a queue so we can update its neighbors later.
We continue this process until the queue is empty, signifying that the updated matrix has stabilized.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/solution1.py):

```python
def bfs(matrix, source):
    updated = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    updated[0][0] = matrix[0][0]
    queue = [source]

    while queue:
        i, j = queue.pop(0)
        for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                alt = updated[i][j] + matrix[x][y]
                if alt < updated[x][y]:
                    updated[x][y] = alt
                    queue.append((x, y))

    return updated
```

The last step is to return the value of the bottom right corner.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0083/solution1.py):

```python
def path_sum_four_ways(filename="matrix.txt"):
    matrix = read_file(filename)
    return dijkstra(matrix, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1))[-1][-1]
```
