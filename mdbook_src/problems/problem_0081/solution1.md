# Dynamic programming

## Problem

This problem is very similar to [Problem 18](../problem_0018/problem.md) and [Problem 67](../problem_0067/problem.md)
However, instead of a triangular structure, we are dealing with square matrix.
The objective is to find the path from the top left corner to the bottom right corner with the smallest sum.

## Understanding the problem

We can use dynamic programming just like in [Problem 18](../problem_0018/problem.md) and [Problem 67](../problem_0067/problem.md).
Starting from the top left corner, we iterate line by line to the bottom right corner.
At each cell, we find which neighboring cell (above or to the left) has the smallest sum and add it to the current cell.
This process is repeated until we reach the bottom right corner.


## Solution

The first step is to read the file and store the matrix in a list of lists.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0081/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return [[int(x) for x in line.split(",")] for line in file.read().splitlines()]
```

The algorithm is straightforward, we just need to take care of the edges cases where we can't go up or left.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0081/solution1.py):

```python
def path_sum_two_ways(filename="matrix.txt"):
    matrix = read_file(filename)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[-1][-1]
```
