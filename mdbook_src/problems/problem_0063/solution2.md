# Back to initial equation

In the [Brute force](./solution1.md) solution, we found that \\( 1 < x < 10 \\) and \\( 10^{n-1} > x^n \\) for \\( n \\) sufficiently large.
Rather than iterating through all \\( n \\) until \\( 10^{n-1} > x^n \\), solving the equation \\( 10^{n-1} = x^n \\) for \\( n \\) gives the exact limit for \\( n \\).

\\[
\begin{align}
&\Leftrightarrow 10^{n-1} = x^n \\\\
&\Leftrightarrow \log_{10}\left(10^{n-1}\right) = \log_{10}\left(x^n\right) \\\\
&\Leftrightarrow n - 1 = n\log_{10}\left(x\right) \\\\
&\Leftrightarrow n(1 - \log_{10}\left(x\right)) = 1 \\\\
&\Leftrightarrow n = \frac{1}{1 - \log_{10}\left(x\right)} \\\\
\end{align}
\\]

Since \\( n \\) is an integer, the limit is the largest integer for which the inequality holds true.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0063/solution2.py):

```python
def powerful_digit_counts():
    return sum(floor(1 / (1 - log10(i))) for i in range(1, 10))
```
