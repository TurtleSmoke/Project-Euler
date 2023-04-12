# Another property of continued fractions

Going back to the equation:

\\[
\frac{\sqrt{N} - b_1}{c_1} = a_2 + \frac{\sqrt{N} - b_2}{c_2}
\\]

and 

\\[
\begin{align}
c_{n+1} &= \frac{N - b_n^2}{c_n}\\\\
a_{n+1} &= \left\lfloor \frac{\sqrt{N} + b_n}{c_{n+1}} \right\rfloor\\\\
b_{n+1} &= -(b_n - a_{n+1}c_{n+1})
\end{align}
\\]

The following can be deduced:

- \\( b_2 < \sqrt{N} \\), because \\( c_2 = \frac{N - b_1^2}{c_1} \\) is positive.
- \\( b_2 \leq a_0 \\), because \\( a_0 = \left\lfloor \sqrt{N} \right\rfloor \\).
- \\( b_2 = a_2c_2 - b_1 \leq a_0 \\)

If \\( a_2 = 2a_0 \\), then \\( b_2 = 2a_0c_2 - b_1 \leq a_0 \\), because all terms are positive integers we have \\( c_2 = 1 \\) and \\( b_1 = a_0 \\).
Which results with \\( b_2 = -(b_1 - a_2c_2) = -(a_0 - 2a_0) = a_0 \\)
The first expression becomes \\( \frac{\sqrt{N} - b_1}{c_1} = a_2 + \frac{\sqrt{N} - b_2}{c_2} = 2a_0 + \frac{\sqrt{N} - a_0}{1} \\)
This is similar to the first iteration of the algorithm, which means that the sequence will repeat when \\( a_n = 2a_0 \\).
The formal proof can be found in the paper [On continued fractions of the square root of prime numbers](https://web.math.princeton.edu/mathlab/jr02fall/Periodicity/alexajp.pdf).

This property is much easier to implement than remembering every \\( b_n \\) and \\( c_n \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0064/solution2.py):

```python
def period_square_roots(n):
    a_0 = floor(sqrt(n))
    if a_0 * a_0 == n:
        return 0

    bn = a_0
    cn = 1

    for pos in itertools.count(1):
        cn = (n - (bn * bn)) / cn
        an = floor((sqrt(n) + bn) / cn)
        bn = -(bn - (an * cn))
        if an == 2 * a_0:
            return pos
```

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0064/solution2.py):

```python
def odd_period_square_roots():
    return sum(period_square_roots(n) % 2 for n in range(2, 10001))
```
