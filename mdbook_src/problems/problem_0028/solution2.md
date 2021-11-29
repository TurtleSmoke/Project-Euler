# Summation

The sum of the diagonals is actually the sum of the 4 corners of each subcube of
the spiral matrix.

With:

\\[
\begin{gather} \color{red}{21}\ 22\ 23\ 24\ \color{red}{25}\\\\ 20\ \ \ \color{red}{7}\ \ \ 8\ \ \ \color{red}{9}\ 10\\\\ 19\ \ \ 6\ \ \ \color{red}{1}\ \ \ 2\ 11\\\\ 18\ \ \ \color{red}{5}\ \ \ 4\ \ \ \color{red}{3}\ 12\\\\ \color{red}{17}\ 16\ 15\ 14\ \color{red}{13}\\\\ \end{gather} \\]

The sum is \\( (1) + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25) \\)

For an \\( n \times n \\) grid, with n being odd, the top right corner is \\( n^
2 \\), the top left corner is \\( n^2 -n + 1 \\), the bottom left corner is \\(
n^2 -2n + 2 \\) and the bottom right corner is \\( n^2 -3n + 3 \\). The sum of
these corners is \\( 4n^2 -6n + 6 \\).

We need to sum these corners for all odd \\( n \\) between 3 and \\( l \\). Odd
numbers can be written in the form \\( 2k + 1 \\). By replacing \\( n \\)
with \\( 2k + 1 \\) we have:

\\[ 4n^2 -6n + 6 = 4(2k+1)^2 -6(2k+1) + 6 = 16k^2 + 4k + 4 \\]

The sum become:

\\[ \begin{align} S &= \sum _{k=1}^{m} 16k^{2} + 4k + 4\\\\ S &= 16\sum _{k=1}^ {m} k^{2} + 4\sum _{k=1}^{m} k + 4\sum _{k=1}^{m} 1\\\\ S &= \frac{16m(m+1) (2m+1)}{6} + \frac{4m(m + 1)}{2} + 4m\\\\ S &= \frac{16m^3}{3} + 10m^2 + \frac{26m}{3}\\\\ \end{align} \\]

where \\( m = \frac{l - 1}{2} \\)

This sum plus \\( 1 \\) (the center of the spiral matrix) is the solution we are
searching for:

```python
def number_spiral_diagonals(n=1001):
    m = (n - 1) // 2
    return int(1 + (16 / 3) * m ** 3 + 10 * m ** 2 + (26 / 3) * m)
```


