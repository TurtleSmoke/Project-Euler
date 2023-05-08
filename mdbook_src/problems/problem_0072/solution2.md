# Farey sequence and Euler's totient function

The [Brute force](solution1.md) solution is inefficient due to the large number of terms in the Farey sequence.
However, it is still possible to use the Farey sequence to solve this problem efficiently.
A Farey sequence of order \\( n \\) is defined as the sequence of irreducible fractions between \\( 0 \\) and \\( 1 \\) whose denominators do not exceed \\( n \\).
The number of terms in the Farey sequence is given by the formula \\( \left | F_n \right | = \left | F_{n-1} \right | + \phi(n) \\), where \\( \phi(n) \\) is Euler's totient function.
Using the fact that \\( \left | F_1 \right | = 2 \\), then \\( \left | F_n \right | = 1 + \sum_{k=1}^{n} \phi(k) \\).

The sum of the totient function is something already done in [Problem 0069](../problem_0069/problem.md).
In this problem, \\( \frac{0}{1} \\) and \\( \frac{1}{n} \\) are not counted, so the answer is \\( \left | F_n \right | = \sum_{k=1}^{n} \phi(k) - 1 \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0072/solution2.py):

```python
def counting_fractions(n=1000000):
    tlist = list(range(n + 1))

    for i in range(1, n + 1):
        p = tlist[i]
        for j in range(2 * i, n + 1, i):
            tlist[j] -= p

    return sum(tlist) - 1
```
