# A better recurrence?

With a bit of algebra, we can explain the recurrence relation in a more elegant way:

\\[
\begin{align}
x_n &= 1 + \frac{a_n}{b_n}\\\\
x_{n+1} &= 1 + \frac{1}{2 + \frac{a_n}{b_n}}\\\\
\end{align}
\\]

It should be clear than \\( 2 + \frac{a_n}{b_n} = 1 + x_n \\), so we can rewrite the second equation as:

\\[
\begin{align}
x_{n+1} &= 1 + \frac{1}{1 + x_n}\\\\
x_{n+1} &= \frac{2 + x_n}{1 + x_n}\\\\
\end{align}
\\]

We are not actually interested in \\( x_{n} \\), but in the numerator and denominator of \\( x_{n} \\), thus if we have \\(x_n = \frac{p_n}{q_n}\\), we can rewrite the last equation as:

\\[
x_{n+1} = \frac{p_{n+1}}{q_{n+1}} = \frac{2 + \frac{p_n}{q_n}}{1 + \frac{p_n}{q_n}} = \frac{\frac{2q_n + p_n}{q_n}}{\frac{q_n + p_n}{q_n}} = \frac{2q_n + p_n}{q_n + p_n}\\\\
\\]

This recurrence is better than the one used in the previous solution, because it explicitly gives the numerator and denominator of \\( x_{n} \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0057/solution2.py):

```python
def square_root_convergents():
    pn = 1
    qn = 1
    count = 0
    for _ in range(1000):
        pn, qn = 2 * qn + pn, qn + pn
        if len(str(pn)) > len(str(qn)):
            count += 1
    return count
```
