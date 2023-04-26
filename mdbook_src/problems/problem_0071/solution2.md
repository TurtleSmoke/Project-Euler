# Farey sequence

The [Brute force](solution1.md) is inefficient because the iterations are not in ascending order of \\( \frac{n}{d} \\).
On way to optimize the solution would be to increase \\( n \\) until \\( \frac{n}{d} > \frac{3}{7} \\) and then decrease \\( d \\) until \\( \frac{n}{d} < \frac{3}{7} \\), stopping just before either condition is met.
However, a much better solution involves using Farey sequences.

A [Farey sequence](https://en.wikipedia.org/wiki/Farey_sequence) is a list of all sorted reduced proper fractions between 0 and 1.

The Farey sequence is constructed by starting with the two fractions \\( \frac{0}{1} \\) and \\( \frac{1}{1} \\) and then inserting the mediant of every adjacent pair of fractions.
Each new fraction \\( \frac{a + c}{b + d} \\) is inserted between \\( \frac{a}{b} \\) and \\( \frac{c}{d} \\).

In this problem, we know that \\( \frac{2}{5} < \frac{3}{7} \\).
Therefore, the solution can be obtained by finding the largest fraction in the Farey sequence with a denominator less than or equal to 1,000,000.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0071/solution2.py):

```python
def ordered_fractions(limit=1000000):
    a, b = 2, 5
    c, d = 3, 7

    while b + d <= limit:
        a, b = a + c, b + d

    return a
```

We can further optimize this solution by noting that \\( b \\) is always updated by adding \\( d \\) until \\( b + d > 1000000 \\).
This operation is performed \\( k = \lfloor \frac{1000000 - b}{d} \rfloor \\) times, so the denominator of the largest fraction is \\( b + kd \\) and the numerator is \\( a + kc \\).
For this problem, the largest numerator is \\( 2 + 3\lfloor \frac{1000000 - 5}{7} \rfloor = 428570 \\).