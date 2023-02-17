# Dynamic programming

The [Brute force](solution1.md) solution has some issue, for example with the
following triangle:

\\[ \\begin{gather} 01\\\\ 02\quad 03\\\\ 04\quad \color{red}{05}\quad 06\\\\ 07\quad \color{green}{08}\quad \color{green}{09}\quad 10\\\\ \end{gather} \\]

The path \\( 1 \rightarrow 2 \rightarrow 5 \\) and the path \\( 1 \rightarrow 3
\rightarrow 5 \\) both end on 5 and then try to find the best solution between 8
and 9. Obviously, the best choice is 9, because it is the largest number between
8 and 9 and there is no path left to take. It doesn't depend on where we come
from, which means that we can replace the number 5 with \\( 5 + 9 = 14 \\). We
can do the same with 4 and 6, which then gives the following triangle:

\\[ \\begin{gather} 01\\\\ 02\quad 03\\\\ \color{red}{12}\quad \color{red}{14}\quad \color{red}{16}\\\\ 07\quad 08\quad 09\quad 10\\\\ \end{gather} \\]

And we can go all the way to the end by reducing the last line each time:

\\[ \\begin{gather} 01\\\\ \color{red}{16}\quad \color{red}{19}\\\\ 12\quad 14\quad 16\\\\ 07\quad 08\quad 09\quad 10\\\\ \end{gather} \\]

And finally:

\\[ \\begin{gather} \color{red}{20}\\\\ 16\quad 19\\\\ 12\quad 14\quad 16\\\\ 07\quad 08\quad 09\quad 10\\\\ \end{gather} \\]

This solution is much faster because it doesn't recalculate anything twice, it
just chooses the best path from the end, since we don't need to know where we
came from to find the best incoming path.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0018/solution2.py):

```python
def maximum_path_sum_I(filename):
    triangle = read_file(filename)

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]
```
