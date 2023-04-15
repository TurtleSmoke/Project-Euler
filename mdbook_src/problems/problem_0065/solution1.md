# Brute force

The problem is to find the sum of the digits in the numerator of the 100th convergent of the continued fraction for \\( e \\).

The key to solve the problem is to understand the pattern of the numerator for each iteration.
By observing the relation between the numerator, denominator and the convergent, the recursive relation should become evident.
Starting with numerators \\( h_1 \\) and \\( h_2 \\), and convergent \\( a_1 \\), the recursive relationship can be defined as follows: \\( h_n = a_n h_{n-1} + h_{n-2} \\).
As the convergent pattern is already given, computing the numerator for the \\( 100 \\)th convergent is a matter of applying the recursive relation \\( 100 \\) times.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0065/solution1.py):

```python
def convergents_of_e():
    an = [2] + [1 if i % 3 != 2 else 2 * (i // 3 + 1) for i in range(1, 100)]
    h1, h2 = 0, 1
    for i in range(100):
        h1, h2 = h2, h1 + an[i] * h2
    return sum(int(c) for c in str(h2))
```
