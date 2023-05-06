# Brute force

The [Problem 0071](../problem_0071/problem.md) teach us that Farey sequences are useful to solve problem involving HCF.
Given two fractions \\( \frac{a}{b} \\) and \\( \frac{c}{d} \\), it is possible to determine the mediant \\( \frac{a+c}{b+d} \\).

In this problem, the first two terms are \\( \frac{0}{1} \\) and \\( \frac{1}{n} \\), with \\( n=1000000 \\).
The next term \\( \frac{p}{q} \\) can be found using the first two terms \\( \frac{a}{b} \\) and \\( \frac{c}{d} \\):

\\[
\frac{a + p}{b + q} = \frac{c}{d}
\\]

Since \\( \frac{c}{d} \\) is in lowest terms, there exists an integer \\( k \\) such that \\( a + p = kc \\) and \\( b + q = kd \\).
Also, \\( \frac{p}{q} - \frac{c}{d} = \frac{cb - da}{d(kd - b)} \\) so the larger the value of \\( k \\), the closer \\( \frac{p}{q} \\) is to \\( \frac{c}{d} \\).
The next term \\( \frac{p}{q} \\) is the one with the largest \\( k \\) such that \\( kd - b \leq n \Leftrightarrow k \leq \frac{n + b}{d} \\).
This gives the following recurrence relation:

\\[
p = \left\lfloor \frac{n + b}{d} \right\rfloor c - a \\\\
q = \left\lfloor \frac{n + b}{d} \right\rfloor d - b
\\]

This relation can be used to generate all the terms of the Farey sequence, in our case, counting the number of terms is enough to solve the problem.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0072/solution1.py):

```python
def counting_fractions(n=1000001):
    a, b, c, d = 0, 1, 1, n
    res = 0

    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        res += 1

    return res
```
