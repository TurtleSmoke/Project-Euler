# Dynamic programming is hidden recursion problem

Another coins problem, another dynamic programming solution !
This solution comes naturally when you try to find the different ways \\( n \\) coins can be separated into piles.

If you were to solve this by hand, you will start with piles of size 1, then of size 2 and one, then of size 3, 2 and one, and so on.
The goal is to find a recurrence relation between \\( p(n, k) \\) and \\( p(n, k+1) \\) where \\( p(n, k) \\) denotes the number of ways to partition \\( n \\) coins into piles of size \\(
k \\) or less.

Consider this table:

<style>
table th {
  position: relative;
}

.line {
  position: absolute;
  height: 33px;
  top: 27px;
  bottom: 0;
  margin: auto;
  left: -6px;
  width: 100%;
  border-top: 1px solid #000;
  transform: rotate(25deg); 
}

.diagonal {
  width: 47px;
}
.diagonal span.lb {
  position: absolute;
  bottom: -2px;
  left: 8px;
}
.diagonal span.rt {
  position: absolute;
  top: -5px;
  right: 7px;
}
</style>

<table>
    <tr>
        <th class="diagonal">
          <span class="lb"><strong>n</strong></span>
          <span class="rt"><strong>k</strong></span>
          <div class="line"></div>
        </th>
        <th><strong>1</strong></th>
        <th><strong>2</strong></th>
        <th><strong>3</strong></th>
        <th><strong>4</strong></th>
        <th><strong>5</strong></th>
    </tr>
    <tr>
        <th><strong>1</strong></th>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <th><strong>2</strong></th>
        <td>1</td>
        <td>2</td>
        <td>2</td>
        <td>2</td>
        <td>2</td>
    </tr>
    <tr>
        <th><strong>3</strong></th>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>3</td>
        <td>3</td>
    </tr>
    <tr>
        <th><strong>4</strong></th>
        <td>1</td>
        <td>3</td>
        <td>4</td>
        <td>5</td>
        <td>5</td>
    </tr>
    <tr>
        <th><strong>5</strong></th>
        <td>1</td>
        <td>3</td>
        <td>5</td>
        <td>6</td>
        <td>7</td>
    </tr>
</table>

Each cell \\( (n, k) \\) represents the number of ways to partition \\( n \\) coins into piles of size \\( k \\) or less.
The recurrence relation closely resembles the of for the [coin sums problem](../problem_0031/solution1.md):

\\[ p(n, k) = p(n, k-1) + p(n-k, k) \\]

The first term represents the number of ways to partition \\( n \\) coins into piles of size \\( k-1 \\) or less, while the second term represents the number of ways to separate \\( n \\) coins using at least one pile of size \\( k \\).
Finally, the base cases are \\( p(0, k) = 1 \\) and \\( p(n, k) = p(n, k -1) \\) if \\( n < k \\).

The rest of the code is relatively straightforward if you understand that you can compute each column of the table one after the other.
Furthermore, since you only care about the remainder of the division by \\( 10^6 \\), you can use the modulo operator to keep the numbers small.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0078/solution1.py):

```python
def coin_partitions(limit=100000):
    divisible_by = 1000000
    cache = [1] * (limit + 1)
    for l in range(2, limit + 1):
        cache[l] = (cache[l] + 1) % divisible_by

        if cache[l] == 0:
            return l

        for n in range(l + 1, limit + 1):
            cache[n] = (cache[n] + cache[n - l]) % divisible_by
```
