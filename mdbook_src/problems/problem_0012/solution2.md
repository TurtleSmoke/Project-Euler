# Common factor

The [Brute Force](solution1.md) solution is really slow, way to slow to be
honest.

First, we can improve the way we find the number of factors. If \\( i \\)
divides \\( n \\), then obviously \\( \frac{n}{i} \\) divides \\( n \\) too. We
do not need to iterate from 2 to \\( n \\) but only to \\( \sqrt{n} \\) and add
the factors two by two. The only exception is that if \\( \sqrt{n} \\) divides
\\( n \\) we only need to count it once.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0012/solution2.py):

```python
def number_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root):
        if n % i == 0:
            res += 1
    return 2 * res + (root**2 == n)
```

This makes the solution much faster, but there is still room for improvement in
the way the triangular numbers are calculated. We already know from the previous
problems that the sum of integer from \\( 1 \\) to \\( n \\) is \\(\frac{n(n+1)
}{2} \\). Since \\( n \\) and \\( n + 1 \\) have no factors in common except \\(
1 \\), we can multiply the number of factor in \\( \frac{n}{2} \\) and \\( n + 1
\\) or \\( n \\) and \\( \frac{n+1}{2} \\) depending on the parity of \\( n \\).
This allows us to calculate the number of factors of smaller numbers, which
makes the solution quite fast compared to the [Brute force](solution1.md)
solution.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0012/solution2.py):

```python
def highly_div_triangular_number(n=500):
    i = 0
    factors = 0
    while factors < n:
        i += 1
        if i % 2 == 0:
            factors = number_of_factors(i // 2) * number_of_factors(i + 1)
        else:
            factors = number_of_factors(i) * number_of_factors((i + 1) // 2)

    return i * (i + 1) // 2
```
