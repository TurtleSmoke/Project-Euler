# Brute force

This problem involves manipulating numerators and denominators of fractions, and understing the recurrence relation between them at each step is the key to solving it.

For example, starting with \\( 1 + \color{red}{\frac{1}{2}} = \frac{3}{2} \\), when computing \\( 1 + \frac{1}{2 + \color{red}{\frac{1}{2}}} = \frac{5}{2} \\), we notice that the denominator is always \\( 2 \\) plus the fraction of the previous equation.

To compute the new numerator and denominator, the first step is to add \\( 2 \\) to the fraction, which is equivalent to adding \\( 2 \times \text{denominator} \\) to the numerator.
The second step is to apply the inverse of the fraction, which simply means swapping the numerator and denominator.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0057/solution1.py):

```python
def new_fraction(numerator, denominator):
    return denominator, 2 * denominator + numerator
```

The last step is to add one to this fraction, which is equivalent of adding the denominator to the numerator.
If the new numerator has more digits than the denominator, increment the counter.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0057/solution1.py):

```python
def square_root_convergents():
    numerator = 0
    denominator = 1
    count = 0
    for _ in range(1000):
        numerator, denominator = new_fraction(numerator, denominator)
        if len(str(numerator + denominator)) > len(str(denominator)):
            count += 1
    return count
```
