# Optimal iteration

The main reason the [Brute force](./solution1.md) approach is slow is that the iteration does not increase \\( D \\) monotonically.
For example, the previous solution tries the values of \\( D \\) in the following order: \\( 4 \\),\\( 7 \\),\\( 11 \\),\\( 10 \\),\\( 17 \\),\\( 21 \\),\\( 13 \\),\\( 23 \\),\\( 30 \\),\\( 34 \\),\\( 16 \\)...

Starting with the smallest possible value of \\( D \\) and increasing it until a solution is found is the optimal iteration approach, as it guarantees the solution with the minimal \\( D \\).
To implement it, we need to iterate through values of \\( D \\).
By definition \\( D = P_d = P_i - P_j \\) where \\( j < i \\), it is necessary to determine a method for computing \\( i \\) and \\( j \\) from \\( d \\).

\\[
\begin{aligned}
P_d &= P_i - P_j\\\\
&= P_{j+x} - P_{j}\\\\
&= \frac{6jx +3x^2 - x}{2}\\\\
&= 3jx + P_x\\\\
&\Rightarrow j = \frac{P_d - P_x}{3x}\\\\
\\end{aligned}
\\]

The following can be concluded from the above equation:

- \\( j \\) must be an integer, so \\( P_d > P_x \\), thus \\( 0 < x < d \\) and \\( P_d - P_x \equiv 0 \pmod{3x} \\).
- \\( P_d - P_x = 3(d^2 - x^2) + d - x \Rightarrow x \equiv d \pmod{3} \\).

Therefore, we can iterate over every \\( d \\) and \\( x \\) such that \\( 0 < x < d \\) and \\( x \equiv d \pmod{3} \\).
If \\( P_d - P_x \equiv 0 \pmod{3x} \\), then we can compute \\( j \\) and \\( i = x + j \\).
By definition, \\( P_d \\) is pentagonal, so if \\( P_i + P_j \\) is also pentagonal, then \\( D = P_d \\) is the solution.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0044/solution2.py):

```python
def pentagon_numbers():
    for d in itertools.count(4):
        pd = pn(d)
        for x in range(d - 3, 0, -3):
            px = pn(x)
            if (pd - px) % (3 * x) == 0:
                j = (pd - px) // (3 * x)
                k = x + j
                if is_pentagonal(pn(k) + pn(j)):
                    return pd
```

