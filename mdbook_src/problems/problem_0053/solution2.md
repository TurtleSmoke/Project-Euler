# Pascal's Triangle

[Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) is a triangular array of the binomial coefficients.
A small example of the Pascal's triangle is depicted below:

\\[
\begin{align}
&1\\\\
&1\ 1\\\\
&1\ 2\ \ 1\\\\
&1\ 3\ \ 3\ \ 1\\\\
&1\ 4\ \ 6\ \ 4\ \ 1\\\\
&1\ 5\ 10\ 10\ 5\ 1\\\\
\end{align}
\\]

The rows of the triangle are indexed from \\( 1 \\) to \\( n \\) and the columns are indexed from \\( 1 \\) to \\( r \\).

It describes the symmetry of the binomial coefficients, which is the reason why it is only necessary to calculate half of the triangle.
Furthermore, if a coefficient is larger than \\( n \\), all coefficients between it and its mirror on the same row will also be larger than \\( n \\).
This observation allows for more efficient iteration over the triangle. **(1)**

Furthermore, recomputing the binomial coefficients is very inefficient, which is why using a cache table for the factorials is a good idea.
Alternatively, the binomial coefficients can be computed using the previous row by applying the following formula:
\\[
\binom{n}{r} = \binom{n - 1}{r - 1} + \binom{n - 1}{r}
\\]

The downside of this approach is that all the coefficients of the previous row have to be computed, which is unnecessary as stated in the first observation.
Therefore, the following formula is used to compute the coefficients, which only requires information about the current row: **(2)**
\\[
\binom{n}{1} = n\\\\
\binom{n}{r} = \dfrac{n - r + 1}{r} \binom{n}{r - 1}
\\]

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0053/solution2.py):

```python
def combinatoric_selections():
    res = 0
    for n in range(23, 101):
        ncr = n
        for r in range(2, n // 2 + 1):
            ncr = (ncr * (n - r + 1)) // r  # Observation 2
            if ncr > 1000000:
                res += n - 2 * r + 1  # Observation 1
                break
    return res
```
