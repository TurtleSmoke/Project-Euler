# Prime Pythagorean triples

Given an arbitrary pair of integers m and n with m > n > 0. Euclid's formula
states that the integers :

\\[ a = m^2 - n^2,\ b=2mn,\ c=m^2+n^2 \\]

form a Pythagorean triple: \\( a^2 + b^2 = c^2 \\)

If we calculate \\( a^2 + b ^2 \\):

\\[ a^2 + b^2 = (m^2-n^2)^2 + (2mn)^2 = m^2 + 4m^2n^2 - 2m^2n^2 + n^2 = (m^2 + n^2)^2 = c^2 \\]

Which is coherent, the problem changes from finding \\( a \\), \\( b \\) and \\(
c \\) to finding \\( m \\) and \\( n \\), we have:

\\[ \begin{align} a+b+c &= 1000\\\\ 2mn + 2m^2 &= 1000\\\\ n &= \frac{500}{m} - m\\\\ \end{align} \\]

We have \\( m > n \\) since b must be positive, solving \\( n = m \\) gives:

\\[ \begin{align} m &= \frac{500}{m} - m\\\\ 0 &= \frac{500 - 2m^2}{m}\\\\ 0 &= 500 - 2m^2\\\\ m &= \sqrt(250)\\\\ \end{align} \\]

Resulting in:

\\[ m > 16 > \sqrt(250) \\]

We also have \\( n > 0 \\), solving \\( n = 0 \\) gives:

\\[ \begin{align} 0 &= \frac{500}{m} - m\\\\ 0 &= 500 - m^2\\\\ m &= \sqrt(500)\\\\ \end{align} \\]

Resulting in:

\\[ m < \sqrt(500) < 23 \\]

We also know that \\( \frac{500}{m} \\) is an integer, so m must divide \\(
500 \\). The only multiple of that divides \\( 500 \\) with the constraint \\(
16 > m > 23 \\) is 20. Having \\( m = 20 \\) result in \\( n = 5 \\). It gives
\\( a = 200 \\), \\( b = 375 \\) and \\( c \\) = 425.

The solution can also be found by using a for loop to find \\( m \\) and \\(
n \\) with the above constraints.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0009/solution3.py):

```python
def special_pythagorean_triplet():
    for m in range(16, 24):
        for n in range(1, m):
            if m * (n + m) == 500:
                return 2 * m * n * (m**4 - n**4)

    return -1
```
