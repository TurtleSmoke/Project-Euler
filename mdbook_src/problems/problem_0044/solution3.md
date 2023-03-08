# Even better iteration

The [Optimal iteration](./solution2.md) approach is much faster than the [Brute force](./solution1.md) approach.
However, for large value of \\( d \\) the iteration through all the possible \\( x \\) is still slow.
Let's try to add more constraints to reduce the numbers of possibility.

The last solution gave the following equation:

\\[
\begin{aligned}
P_d & = P_i - P_j\\\\
\Leftrightarrow d(3d - 1) &= i(3i - 1) - j(3j - 1) \\\\
&= (i - j)(3(i + j) - 1) \\\\
\end{aligned}
\\]

The following can be concluded from the above equation:

- \\( i - j \equiv 0 \pmod{d(3d + 1)} \\).
- Since \\( i \\), \\( j \\), and \\( d \\) are positive integers, it follows that \\( 0 < i - j < d \\) because if \\( d < i - j \\), then \\( 3d - 1 < 3(i - j) - 1 < 3(i + j) - 1 \\) which implies that \\( d(3d - 1) < (i - j)(3i - 3i - 1) \\) because \\(d, i, j \\), a contradiction.
- \\( i - j \equiv d \pmod{3} \\) because \\( 3d - 1 \equiv 3(i + j) - 1 \equiv 2 \pmod{3} \\).

To summarize, we are searching for all \\( i \\) and \\( j \\) that satisfy:
\\[
\begin{align}
&i\text{ and }j\text{ are positive integers.} \tag{0}\\\\
&0 < i - j < d \tag{1}\\\\
&i - j \equiv d \pmod{3} \tag{2}\\\\
&3(i + j) - 1 \equiv 2 \pmod{3} \tag{3}\\\\
&i - j \equiv 0 \pmod{d(3d + 1)} \tag{4}\\\\
\end{align}
\\]

The solution can be found by iterating through all values of \\( d \\) and find all divisors \\( r_1 = i - j \\) that satisfy equation \\( 3 \\) and \\( 4 \\).

If \\( i = \frac{r_1 + \frac{(r_2 + 1)}{3}}{2} \\) is an integer (equation 0), then \\( j = i - r_1 \\).
If both \\( P_i \\) and \\( P_j \\) are pentagonal numbers, then the solution is \\( P_d \\).

It is important to know that this approach is not as efficient as the previous one for small values of \\( d \\), but it is significantly faster for large values of \\( d \\), especially if the function for obtaining all the divisors of \\( d(3d + 1) \\) is optimized.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0044/solution3.py):

```python
def pentagon_numbers():
    pn = lambda n: n * (3 * n - 1) // 2
    for d in itertools.count(4):
        for r1 in get_divisors(d):  # Equation 4
            r2 = d * (3 * d - 1) // r1
            if r2 % 3 == 2:  # Equation 3
                i = (r1 + (r2 + 1) // 3) / 2
                if i.is_integer():  # Equation 0
                    j = i - r1
                    if is_pentagonal(pn(i) + pn(j)):
                        return pn(d)
```

It is also worth noting that the pandigital number could be cached, as many of them are computed multiple times.
