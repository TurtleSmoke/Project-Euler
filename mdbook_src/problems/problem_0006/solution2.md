# Summation formula

We learned in [Problem 1: Multiples of 3 and 5](../problem_0001/problem.md)
that:

\\[ \sum{k} = \frac{n(n+1)}{2} \\]

This gives the following formula for the square of the sum:

\\[ (1+2+...+10)^2 = \left(\sum{k}\right)^2 = \left(\frac{n(n+1)}{2}\right)^2 = \frac{n^2 (n+1)^2}{4} \\]

The sum of the squares can be found using the formula:

\\[ \sum{k^2} = \frac{n(n+1)(2n+1)}{6} \\]

There are many demonstrations to prove this equation, let's just look at one of
them:

\\[ \begin{align} ( k-1)^{3} &=k^{3} -3k^{2} +3k-1\\\\ k^{3} -( k-1)^{3} &=3k^{2} -3k+1\\\\ \sum _{k=1}^{n}\left( k^{3} -( k-1)^{3}\right) &=\sum _{k=1}^{n} 3k^{2} -3k+1 \\\\ \sum _{k=1}^{n} k^{3} -\sum _{k=1}^{n}( k-1)^{3} &=3\sum _{k=1}^{n} k^{2} -3\sum _{k=1}^{n} k+\sum _{k=1}^{n} 1\\\\ \sum _{k=1}^{n} k^{3} -\sum _{k=0}^{n-1} k^{3} &=3\sum _{k=1}^{n} k^{2} -3\frac{n( n+1)}{2} +n\\\\ n^{3} &=3\sum _{k=1}^{n} k^{2} -3\frac{n( n+1)}{2} +n\\\\ \sum _{k=1}^{n} k^{2} &=\frac{1}{3} n^{3} +\frac{n( n+1)}{2} -\frac{1}{3} n\\\\ \sum _{k=1}^{n} k^{2} &=\frac{n( n+1)( 2n+1)}{6} \end{align} \\]

The solution can be found in constant time with these two equations:

\\[ \frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6} = \frac{3n^4+2n^3-3n^2-2n}{12} \\]

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0006/solution2.py):

```python
def sum_square_difference(n=100):
    return (3 * n**4 + 2 * n**3 - 3 * n**2 - 2 * n) // 12
```
