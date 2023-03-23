# Observation is insight

Although the [Brute force](solution1.md) approach can effectively solve the problem, exploring alternative methodologies can offer valuable insights.
In this case, several pertinent observations can be made:

1. The number must be a multiple of \\( 9 \\), because every number are congruent to the sum of their digits modulo \\( 9 \\), thus \\( x \equiv s \pmod{9} \\), where \\( s \\) is the sum of digits of \\( x \\).
  Since \\( 2x \equiv s \pmod{9} \\), it follows that \\( 2x - x \equiv s - s \pmod{9} \\), which implies that \\( x \equiv 0 \pmod{9} \\).
2. The first digit of the number must be \\( 1 \\), otherwise \\( 2x \\) would have one more digit than \\( x \\).
3. According to the previous observation, \\( 2x \\) must start with \\( 2 \\) or \\( 3 \\), \\( 3x \\) must start with \\( 3 \\) or \\( 4 \\) and so on.
  Therefore, the number must at least contain 6 digits to satisfy to contain digits from \\( 1 \\) to \\( 6 \\).
4. The number must contain a \\( 0 \\) or a \\( 5 \\) because \\( 5x \\) is obviously a multiple of \\( 5 \\).

It's actually possible to continue with the observation and find the solution by hand.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0052/solution2.py):

```python
def permuted_multiples():
    for i in itertools.count(100008, 9):  # Observation 1 and 4
        s = str(i)
        if int(s[0]) != 1 or all(d not in s for d in "05"):  # Observation 2 and 3
            continue
        if all(sorted(s) == sorted(str(i * j)) for j in range(2, 7)):
            return i
```

It is worth noting that the solution is trivial if one know the property of [\frac{1}{7}](https://en.wikipedia.org/wiki/7#In_decimal) in decimal representation.
