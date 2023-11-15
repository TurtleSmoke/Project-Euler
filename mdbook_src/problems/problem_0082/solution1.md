# Dynamic programming

## Problem

The problem is the exact same as [Problem 81](../problem_0081/problem.md), but this time, we can go up.

## Understanding the solution

In this problem, moving up **and** down multiple times within the same column is allowed.
However, the optimal path won't go both up and down within the same column.
That would be wasting steps because every cell has a positive value.
So if we iterate from top to bottom, we only need to know if the cell above has been updated.
Similarly, if we iterate from bottom to top, we only need to know if the cell below has been updated.

Now, let's take a look at this example where we iterate from left to right for the first column: 

\\[
\begin{bmatrix}
\color{red}{1} & 1 & 10\\\\
\color{red}{10} & 1 & 10\\\\
\color{red}{15} & 1 & 1
\end{bmatrix} \Longrightarrow \begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{red}{11} & 10\\\\
15 & \color{red}{16} & 1
\end{bmatrix}\\\\
\\]

Nothing fancy here; we add the left cell's value to the current cell.
Now, let's iterate from top to bottom for this column, updating the green cell:

\\[
\begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{green}{11} & 10\\\\
15 & \color{red}{16} & 1
\end{bmatrix} \rightarrow (\color{red}{2} + 1) < \color{green}{11}\rightarrow \begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{red}{3} & 10\\\\
15 & \color{green}{16} & 1
\end{bmatrix} \rightarrow (\color{red}{3} + 1) < \color{green}{16}\rightarrow \begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{red}{3} & 10\\\\
15 & \color{red}{4} & 1
\end{bmatrix}\\
\\
\\]

During the update, we're comparing the <span style="color:green">current cell's updated value</span> with the <span style="color:red">above cell updated value</span> plus the current cell's initial value.
For this case, \\( \color{green}{11} \\) is compared with \\( \color{red}{2} + 1 \\).
Keep repeating this process until you reach the column's bottom, then do the same from bottom to top:

\\[
\begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{green}{3} & 10\\\\
15 & \color{red}{4} & 1
\end{bmatrix} \rightarrow (\color{red}{4} + 1) > \color{green}{3}\rightarrow \begin{bmatrix}
1 & \color{green}{2} & 10\\\\
10 & \color{red}{3} & 10\\\\
15 & \color{red}{4} & 1
\end{bmatrix} \rightarrow (\color{red}{3} + 1) > \color{green}{2}\rightarrow \begin{bmatrix}
1 & \color{red}{2} & 10\\\\
10 & \color{red}{3} & 10\\\\
15 & \color{red}{4} & 1
\end{bmatrix}\\
\\
\\]

## Implementation

The first step is to read the file and store the matrix, in this case, in a list of lists.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0082/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return [[int(x) for x in line.split(",")] for line in file.read().splitlines()]
```

The main challenge is handling the top-to-bottom and bottom-to-top iterations.
Since we need to keep track of both the updated columns and initial columns, updating the matrix in place won't work.
Instead, we can create a copy of the first column that will represent the updated values of the current column's smallest path.

So, when updating from left to right, we simply add to this copy the value of the initial cell of the right column.
When updating from top to bottom, we compare the updated value of the current cell with the updated value of the cell above plus the initial value of the current cell.
The process is the same for the bottom-to-top iteration.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0082/solution1.py):

```python
def path_sum_three_ways(filename=".txt"):
    rows = read_file(filename)
    current = [r[0] for r in rows]

    for x in range(1, len(rows[0])):
        for y in range(len(rows)):  # Left to right
            current[y] += rows[y][x]
        print(current)
        for y in range(1, len(rows)):  # Top to bottom
            current[y] = min(current[y], current[y - 1] + rows[y][x])
        for y in range(len(rows) - 2, -1, -1):  # Bottom to top
            current[y] = min(current[y], current[y + 1] + rows[y][x])

    return min(current)
```

The answer is the minimum value of the copied column after we have iterated through the whole matrix.