# Dynamic programming

The last solution does not scale to the number of parts or the target. We can do
better using dynamic programming, but first, we must divide the problem into
subproblems.

Let's start with the ways to do 1p using all the pieces we have. The table is a
cumulative sum, so the value of each cell is the number of ways to have the
target using the pieces up to the current one. We consider that there is only
one way to do 0p, so the first column is always 1.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 0p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |

This table means that there is only one way to express 1p, no matter what coins
we are using.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 0p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 2p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |

2p can be expressed using 1p: 1p + 1p, but also using 2p. With the other coins
the result remain the same.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 0p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 2p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |
| 3p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |
| 4p  |  1  |       3       |       3       |       3        |       3        |       3        |        3        |        3        |
| 5p  |  1  |       3       |       4       |       4        |       4        |       4        |        4        |        4        |

You might start to understand how this table was computed:

* The first column is always 1, there is only one way to express any target
  with 1p.
* The first row is always 1, there is only one way to express 0p.
* For the rest we construct the table lines by lines, the current cells is the
  sum of two possibilities:
    * The new coin is not used,
    * The new coin is not used: the number of ways to make \\( n \\) is the
      number of way to make \\(n - 1 \\) using the same coins, which is the
      value in the left cell.
    * If possible, the new coin is used: the number of ways to make \\( n \\) is
      the number of ways to make \\( n - c \\) using the same coins, which is
      the value in the cell on the same column but on the line \\( n - c \\).

For example with the last line, the first column is obviously 1
and the second is: 1 (left cell) + 2 (the number of ways to make \\( 5p -
2p = 3p \\), above cell).

So, using a cache table, we can drop the time complexity from \\( O(m^n) \\) to
\\( O(nm) \\), where \\( n \\) is the target and \\( m \\) the number of
coins. But we now have an \\( O(nm) \\) space complexity.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0031/solution2.py):

```python
def coin_sums(n=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [[1] + [0] * (len(coins) - 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(1, len(coins)):
            cache[i][j] = cache[i][j - 1]
            if coins[j] <= i:
                cache[i][j] += cache[i - coins[j]][j]

    return cache[-1][-1]
```
