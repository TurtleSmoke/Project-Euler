# Brute force

The problem can be decomposed into two distinct tasks:

- Verification whether a number is pentagonal or not.
- Determination of the lower bound for the iteration through pentagonal pairs.

The first task can be approached similarly to [problem 42](../problem_0042/solution1.md), by using the equation \\( x = \frac{1}{2}n(3n-1) \\) and searching for \\( n \\).

\\[
    x = \frac{1}{2}n(3n-1) \Rightarrow 3n^2 - n - 2x = 0 \Rightarrow n = \frac{\pm \sqrt{1 + 24x} + 1}{6}
\\]

Since we are only concerned with positive integers, the negative solution \\( \frac{- \sqrt{1 + 24x} + 1}{6} \\) can be disregarded.
There, a number is pentagonal if \\( \frac{\sqrt{1 + 24x} + 1}{6} \\) is an integer.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0044/solution1.py):

```python
def is_pentagonal(n):
    return ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()
```

The second task is a bit more tricky since there is no obvious lower bound to terminates the iteration.
The only constraints is that that solution \\( D \\) must be minimal.
As the sequence of pentagonal numbers is strictly increasing, at some point, the difference between two successive numbers will exceed the current result.
Consequently, the iteration can be stopped, as all subsequent numbers will also surpass the current solution.

The difference between \\( P_n \\) and \\( P_{n+1} \\) is:
\\[ P_{n+1} - P_n = \frac{1}{2}(n+1)(3(n+1)-1) - \frac{1}{2}n(3n-1) = 3n + 1 \\]

Hence, the iteration should stop when \\( 3n + 1 > D \\), which is finite assuming there is a solution.

The approach is to iterate through all pairs of pentagonal numbers \\( P_i \\) and \\( P_j \\) with \\( j < i \\) and verify if both \\( P_i + P_j \\) and \\( P_i - P_j \\) are pentagonal.
If they are, we have found a solution, and the iteration continues until \\( 3 * i + 1 > D \\), at which point the current result is the final solution.

To optimize the search, it is more efficient to iterate backwards through \\( P_j \\) since we are searching for the smallest \\( D \\) that satisfies the condition.
When \\( P_i - P_j > D \\), the iteration through \\( P_j \\) can be stopped.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0044/solution1.py):

```python
def pentagon_numbers():
    res = float("inf")
    pn = lambda n: n * (3 * n - 1) // 2
    for i in itertools.count(2):
        if 3 * i + 1 > res:
            break
        for j in range(i - 1, 0, -1):
            a = pn(i)
            b = pn(j)
            if a - b > res:
                break
            if is_pentagonal(a + b) and is_pentagonal(a - b) and a - b < res:
                res = a - b
    return res
```

