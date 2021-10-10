# Fibonacci convergence

We know from [Fibonacci and the golden ratio](../problem_0002/solution3.md)
that the n-th term of Fibonacci can be expressed as :

\\[ F_{n} = \frac{\varphi^{n}}{\sqrt{5}} = \frac{\left(\frac{1+\sqrt{5}}{2}
\right)^n}{\sqrt{5}} \\]

Searching for a number with at least 1000 digit is the same as searching a
for number that is greater than or equal to \\( 10^{999} \\)

\\[ \begin{align} \frac{\varphi^{n}}{\sqrt{5}} & >= 10^{999}\\\\
n * \log(\varphi) - \frac{\log(5)}{2} & >= 999 * log(10)\\\\
n & >= \frac{\frac{\log(5)}{2} + 999}{\log(\varphi)}\\\\ 
n & = \left\lceil\frac{\frac{\log(5)}{2} + 999}{\log(\varphi)} \right\rceil\\\\ \end{align} \\]

Since n must be an integer, it is sufficient to take the ceiling from the
previous equation.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0025/solution2.py):

```python
def thousandth_digit_fibonacci_number(n=1000):
    return ceil((n - 1 + log10(sqrt(5)) / 2) / log10((1 + sqrt(5)) / 2))
```
