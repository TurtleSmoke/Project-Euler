# Lucky numbers of Euler

Thanks
to [mathworld](https://mathworld.wolfram.com/Prime-GeneratingPolynomial.html)
, we know that if \\( p(n) = n^2 + n + 41 \\) is prime-generating for \\(
0 \leq n \leq L \\), then so is \\( p(L - n) \\).

\\[ \begin{align} &p(n) = n^2 + n + 41\\\\ &p(L - n) = (L - n)^2 + L - n + 41\\\\ &p(L - n) = L^2 - 2Ln + n^2 + L - n + 41\\\\ &p(L - n) = n^2 - (2L + 1)n + L^2 + L + 41\\\\ &p(L - n) = n^2 - (2L + 1)n + p(L)\\\\ &p(L - n) = n^2 + an + b\\\\ &where\ a = -(2L + 1)\ and\ b = L^2 + L + 41\\\\ \end{align} \\]

We also know from the [Shorten the intervals](solution2.md) solution that when
\\( n = 0 \\), \\( b = L^2 + L + 41 \\) is prime. Since \\( |b| < 1000 \\) we
have:

\\[ b = L^2 + L + 41 < 1000 \Rightarrow -31 \leq L \leq 31 \\]

We also know that \\( b \\) is the upper limit of consecutive primes, it means
that \\( b \\) must be the largest number possible. It corresponds to \\( L = 30
\\) and \\( b = 30^2 + 30 + 41 = 971 \\) and \\( a = -(2 \times 30 + 1)
= -61 \\).

We can find a general solution based on the limit by searching the value of \\(
L \\) and then computing \\( a \times b = (L^2 + L + 41) \times (-2(L + 1))
\\).

The value of \\( L \\) is the largest solution for \\( L^2 + L + 41 < limit \\)
.\
We have \\( \Delta = 1 - 4(41 - limit) \\), thus the solution is L = 
\\( \left\lfloor \frac{-1 + \sqrt{4(41 - limit)}}{2} \right\rfloor \\)

```python
def quadratic_primes(limit=1000):
    l = floor((-1 + sqrt(1 - 4 * (41 - limit))) / 2)
    return (l ** 2 + l + 41) * (-(2 * l + 1))
```