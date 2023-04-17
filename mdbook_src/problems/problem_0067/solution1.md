# Dynamic programming 

This problem is the same as [Problem 0018](../problem_0018/problem.md), but with a larger triangle.

As we did in the [Dynamic programming](../problem_0018/solution2.md) solution for Problem 0018, we can reduce the triangle by replacing each number with the sum of itself and the largest number below it.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0067/solution1.py):

```python
def maximum_path_sum_II(filename):
    triangle = read_file(filename)

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]
```
