# Brute force

The first step is to identify curious faction, such as \\( \frac{49}{98} \\).
A Curious faction can take one of four forms, which can be expressed as follows:

\\[
\frac{ax}{bx} = \frac{a}{b} \Rightarrow \frac{10a + x}{10b + x} = \frac{a}{b} \Rightarrow 10ab + bx = 10ab + ax \Rightarrow x(a - b) = 0
\\]

This implies that either \\( x = 0 \\) or \\( a = b \\). Both solutions are trivial.

\\[
\frac{xa}{xb} = \frac{a}{b} \Rightarrow \frac{10x + a}{10x + b} = \frac{a}{b} \Rightarrow 10bc + ba = 10ax + ab \Rightarrow x(a - b) = 0
\\]

This yields the same trivial solutions as the first case.

The only non-trivial solutions are of the form \\( \frac{ax}{xb} \\) or \\( \frac{xa}{bx} \\).
We simply need to determine whether we are dealing with the first or second case and verify whether the fractions are the same with and without \\( x \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0033/solution1.py):

```python
def is_curious_fraction(numerator, denominator):
    if numerator % 10 == denominator // 10:
        return abs((numerator / denominator) - (numerator // 10 / (denominator % 10))) < 0.0000001
    elif numerator // 10 == denominator % 10:
        return abs((numerator / denominator) - (numerator % 10 / (denominator // 10))) < 0.0000001
    return False
```

To ensure accuracy in the presence of floating-point values, the returned value must be compared to a small value to ensure it is close enough to zero.

The second step is to iterate over every fraction, with the numerator being smaller than the denominator, as all fractions must be smaller than 1.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0033/solution1.py):

```python
def digit_cancelling_fractions():
    final_numerator, final_denominator = 1, 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 or denominator % 10 == 0:
                continue
            if is_curious_fraction(numerator, denominator):
                final_numerator *= numerator
                final_denominator *= denominator

    return final_denominator // gcd(final_numerator, final_denominator)
```
