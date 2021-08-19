# Fibonacci and the golden ratio

Although the number of iterations of the second solution is lower than that of
the first solution, it is possible to do better:

\\[ \begin{align} \frac{1}{4}(E_{n+1} + E_{n} - 2) &= \frac{1}{4}(F_{3(n+1)} + F_{3n} - 2)\\\\ &= \frac{1}{4}(F_{3n+2} + F_{3n+1} + F_{3n} - 2)\\\\ &= \frac{1}{4}(2F_{3n+2} - 2)\\\\ &= \frac{1}{2}(F_{3n+2} - 1)\\\\ \end{align} \\]

This does not really change the problem, since we still need to iterate until
\\( F_{3n} \\) reach the limit and then compute \\(\frac{1}{2}(F_
{3n+2} - 1)\\).

Actually, the Fibonacci numbers can be approximated with the following
[equation](https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression):

\\[ F_{n} = \frac{\varphi^{n} - (-\varphi)^{-n}}{\sqrt{5}} \\]

where \\( \varphi = \frac{1+\sqrt{5}}{2} \\) is the
[golden ratio](https://en.wikipedia.org/wiki/Golden_ratio).

\\( -(-\varphi)^{-n} \\) can be ignored for large numbers which gives the
equation:

\\[ F_{n} = \frac{\varphi^{n}}{\sqrt{5}} \\]

The limit is the n-th Fibonacci number such that:

\\[ \begin{align} F_{n} &\leqslant M\\\\ \frac{\varphi ^{n}}{\sqrt{5}} &\leqslant M\\\\ \varphi ^{n} &\leqslant \sqrt{5} M\\\\ n\log( \varphi ) &\leqslant \log\left(\sqrt{5} M\right)\\\\ n &\leqslant \left\lfloor \frac{\log\left(\sqrt{5} M\right)}{\log( \varphi )} \right\rfloor \end{align} \\]

The result can be computed with \\(\frac{1}{2}(F_{n+2} - 1) \\) where \\( n =
\left\lfloor \frac{\log\left(\sqrt{5} M\right)}{\log( \varphi )} \right\rfloor
\\):

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0002/solution3.py):

```python
def sum_of_even_fibonacci_numbers(limit=4000000):
    golden_ratio = (1 + sqrt(5)) / 2
    n = floor(log(sqrt(5) * limit) / log(golden_ratio))
    fn = round((golden_ratio**(n + 2)) / sqrt(5))

    return (fn - 1) // 2
```
