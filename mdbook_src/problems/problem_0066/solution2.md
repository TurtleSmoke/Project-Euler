# Solving Pell's equations

This diophantine equation is called [Pell's equation](https://en.wikipedia.org/wiki/Pell%27s_equation), and it is possible to solve it using the [continued fraction](https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions) expansion of \\( \sqrt{D} \\).

This method involves finding the numerator and denominator of the \\( i \\)-th convergent of \\( \sqrt{D} \\) denoted by \\( h_i \\) and \\( k_i \\) respectively, where \\( h_i^2 - D k_i^2 = 1 \\) for some \\( i \\).
Furthermore, the first \\( i \\) that satisfies this condition corresponds to the smallest \\( x \\) that satisfies the equation.

With [Problem 0065](../problem_0065/problem.md), we know the recurrence relation for computing \\( h_i \\) and \\( k_i \\) is:

\\[
h_i = a_i h_{i-1} + h_{i-2}\\\\
k_i = a_i k_{i-1} + k_{i-2}
\\]

where \\( a_i \\) is the \\( i \\)-th convergent of \\( \sqrt{D} \\).

The cycle of convergent of \\( \sqrt{D} \\) can be computed using the method [Another property of continued fractions](../problem_0064/solution2.md).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0066/solution2.py):

```python
def get_convergent_cycle(n):
    a_0 = floor(sqrt(n))
    res = []
    if a_0 * a_0 == n:
        return []

    bn = a_0
    cn = 1

    for _ in itertools.count(1):
        cn = (n - (bn * bn)) / cn
        an = floor((sqrt(n) + bn) / cn)
        bn = -(bn - (an * cn))
        res.append(an)
        if an == 2 * a_0:
            return res
```

Then, using the recurrence relation, we can compute \\( h_i \\) and \\( k_i \\) and find the first \\( i \\) that satisfies \\( h_i^2 - D k_i^2 = 1 \\) for each \\( D \leq 1000 \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0066/solution2.py):

```python
def diophantine_equation():
    x, res = 0, 0
    for d in range(2, 1001):
        an = get_convergent_cycle(d)
        if not an:
            continue

        h1, h2, k1, k2 = 1, floor(sqrt(d)), 0, 1
        for i in itertools.count(0):
            h1, h2 = h2, h1 + an[i % len(an)] * h2
            k1, k2 = k2, k1 + an[i % len(an)] * k2
            if h2 * h2 - d * k2 * k2 == 1:
                x, res = max((h2, d), (x, res))
                break

    return res
```
