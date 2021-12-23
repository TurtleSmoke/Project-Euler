# Dynamic programming

To solve problem using dynamic programming, we need to divide the problem into
sub-problems. So let's try to do that.

Let's take for example 5 pences:
How many different ways can 5 pences be made using any number of coins?

Let's start with the ways of doing 1p using all the piece we have.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |

This table means that there is only one way to express 1p, no matter what coins
we are using.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 2p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |

2p can be expressed using 1p: 1p + 1p, but also using 2p. With the other coins
the result remain the same.

|     |  1  | \\( \leq \\)2 | \\( \leq \\)5 | \\( \leq \\)10 | \\( \leq \\)20 | \\( \leq \\)50 | \\( \leq \\)100 | \\( \leq \\)200 |
|:---:|:---:|:-------------:|:-------------:|:--------------:|:--------------:|:--------------:|:---------------:|:---------------:|
| 1p  |  1  |       1       |       1       |       1        |       1        |       1        |        1        |        1        |
| 2p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |
| 3p  |  1  |       2       |       2       |       2        |       2        |       2        |        2        |        2        |
| 4p  |  1  |       3       |       3       |       3        |       3        |       3        |        3        |        3        |
| 5p  |  1  |       3       |       4       |       4        |       4        |       4        |        4        |        4        |

You might start to understand how this table was computed:

* The first column is always 1, there is only one way to express \\( n \\)
  using 1p coins.
* Each time we try a new coin, we take the result on the left, which is the
  number of ways to make the total without using the current coin plus the
  number of ways we can form target minus the current coin, which is the number
  of ways to form the remainder if we subtract the coin from the target.

For example with the last line with target 5p, The first column is obviously 1
and the second is 1 (from the column one) + the number of ways to make \\( 5p -
2p = 3p \\), which was calculated earlier.

To put it in a nutshell, we must create a table of 8 columns (number of
different coins) and 201 lines (0p to 200p). The first column will always be 1
and our goal is to find the value in the bottom right corner. We must compute
each cell, from left to right and up to down by adding the cell on the left
(reach the target without the current coin) plus the cell in the same column but
on the line target minus current coin if the current coin is less than the
target (reach the target using the current coin).

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