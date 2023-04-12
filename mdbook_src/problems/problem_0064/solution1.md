# Brute force

The solution asks for the number of continued fractions with an odd period.
A continued fraction is an expression obtained through an iterative process of representing a number as the sum of its integer part and the reciprocal of another number, then writing this other number as the sum of its integer part and another reciprocal, and so on. <sup>[1](https://www.britannica.com/science/continued-fraction)</sup>

To solve the problem, the first step is to understand the iterative nature of the continued fractions.

The continued fraction is defined using \\( a_0 = \left\lfloor \sqrt{N} \right\rfloor \\) as:
\\[
\begin{align}
\sqrt{N} &= a_0 + \sqrt{N} - a_0\\\\
&= a_0 + \frac{1}{\frac{1}{\sqrt{N} - a_0}} = a_0 + \frac{1}{\frac{\sqrt{N} + a_0}{N - a_0^2}} = a_0 + \frac{1}{a_1 + \frac{\sqrt{N} - b_1}{c_1}}\\\\
\end{align}\\\\
\text{where } c_1 = N - a_0^2; \quad a_1 = \left\lfloor \frac{\sqrt{N} + a_0}{c_1} \right\rfloor; \quad b_1 = -(a_0 - a_1c_1)
\\]

Repeating the process gives:

\\[
\begin{align}
a_1 + \frac{\sqrt{N} - b_1}{c_1} &= a_1 + \frac{1}{\frac{c_1}{\sqrt{N} - b_1}} = a_1 + \frac{1}{\frac{\sqrt{N} + b_1}{\frac{N - b_1^2}{c_1}}} = a_1 + \frac{1}{a_2 + \frac{\sqrt{N} - b_2}{c_2}}\\\\
\end{align}\\\\
\text{where } c_2 = \frac{N - b_1^2}{c_1}; \quad a_2 = \left\lfloor \frac{\sqrt{N} + b_1}{c_2} \right\rfloor; \quad b_2 = -(b_1 - a_2c_2)
\\]

The process can be continued, and the following pattern can be observed:

\\[
\begin{align}
c_{n+1} &= \frac{N - b_n^2}{c_n}\\\\
a_{n+1} &= \left\lfloor \frac{\sqrt{N} + b_n}{c_{n+1}} \right\rfloor\\\\
b_{n+1} &= -(b_n - a_{n+1}c_{n+1})
\end{align}
\\]

The first equation can be rewritten as \\( a_0 + \sqrt{N} - a_0 = a_0 + \frac{\sqrt{N} - a_0}{1} = a_0 + \frac{\sqrt{N} - b_0}{c_0} \\) which results in the same pattern as the second equation and provides the initialisation for the iterative process.
The iteration can be stopped when \\( b_n \\) and \\( c_n \\) repeat, because the continued fraction will also repeat itself.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0064/solution1.py):

```python
def period_square_roots(n):
    a_0 = floor(sqrt(n))
    if a_0 * a_0 == n:
        return 0

    bn = a_0
    cn = 1
    remainders = {}

    for pos in itertools.count(1):
        cn = (n - (bn * bn)) / cn
        an = floor((sqrt(n) + bn) / cn)
        bn = -(bn - (an * cn))
        if (bn, cn) in remainders:
            return pos - remainders[bn, cn]
        remainders[bn, cn] = pos
```

The solution can be computed by trying all the numbers \\( N \\) below \\( 10000 \\) and counting the number of continued fractions with an odd period.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0064/solution1.py):

```python
def odd_period_square_roots():
    return sum(period_square_roots(n) % 2 for n in range(2, 10001))
```
