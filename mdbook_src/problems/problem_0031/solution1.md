# Brute force

We are searching for all the combination to make 2 pounds using the eights
following coins in pence:
> 1, 2, 5, 10, 20, 50, 100, 200.

Combination implies that making 2 pounds with `100 + 50 + 50` pences is the same
as `50 + 100 + 50` pences. To avoid this, we will try every piece one by one in
increasing order.

The algorithm will use an accumulator that will increase with each iteration of
the function:

1. If the accumulator reaches 200, a combination has been found.
2. If the accumulator is greater than 200 the current combination will not work.
3. If the accumulator is less than 200, add a new piece. To avoid duplicate
   combinations, always add piece larger than or equal to the last one.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0031/solution1.py):

```python
def coin_sums(n=200):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    def coin_sums_rec(accumulator, minimum_piece):
        if accumulator == n:
            return 1
        if accumulator > n:
            return 0

        return sum(coin_sums_rec(accumulator + coins[new_piece], new_piece)
                   for new_piece in range(minimum_piece, len(coins)))

    return coin_sums_rec(0, 0)
```