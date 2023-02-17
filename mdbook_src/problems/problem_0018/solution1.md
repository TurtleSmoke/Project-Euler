# Brute force

Even if the problem tells us not to use brute force, we will still do it. Not
because we want to do things easily, but because it will be much easier to find
a better solution later after solving the problem the first time.

First, we need to transform the triangle into something easier to manipulate,
for example a two-dimensional array.

The problem can be solved quite easily after that, with a simple recursion: The
maximum score is the current number plus the highest score by choosing the left
or the right.

It is enough to stop when we are outside the triangle, since the lower number is
0, we can consider that leaving the triangle is like adding 0.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0018/solution1.py):

```python
def maximum_path_sum_I(filename):
    triangle = read_file(filename)

    def path(i, j):
        if i >= len(triangle) or j >= len(triangle[i]):
            return 0

        return triangle[i][j] + max(path(i + 1, j), path(i + 1, j + 1))

    return path(0, 0)
```
