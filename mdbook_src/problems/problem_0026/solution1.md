# Brute force

How do you find the decimals of a fraction?

In elementary school, we learned a method to convert fractions to decimals.
Repeat the process of multiplying the numerator by 10:

* The next numerator is the rest of the Euclidean division by the denominator.
* The quotient is the next decimal.

For example with \\( \frac{1}{7} \\):

\\[ \begin{align} \frac{1}{7} &= 7 * \mathbf{0} + 1\\\\ \frac{10}{7} &= 7 * \mathbf{1} + 3\\\\ \frac{30}{7} &= 7 * \mathbf{4} + 2\\\\ \frac{20}{7} &= 7 * \mathbf{2} + 6\\\\ \frac{60}{7} &= 7 * \mathbf{8} + 4\\\\ \frac{40}{7} &= 7 * \mathbf{5} + 5\\\\ \frac{50}{7} &= 7 * \mathbf{7} + 1\\\\ \frac{10}{7} &= \dots\\\\ \end {align} \\]

That give us \\( \frac{1}{7} = 0,142857... \\).

We just have to pay attention to some special cases:

* When the rest is 0, the division is finite and there is no cycle. We can
  assume that the length of the cycle is 0.
* The length of the cycle is not the number of time we repeat the process of
  finding the decimals of a fraction. For example with \\( \frac{1}{6} = 0,
  166... \\) the cycle is 1. But there is some leading number before it.

Detecting the cycle is possible using a set. But we will have no way of knowing
when it started, which is required to find its length. We need to store both the
numbers and their positions for every decimal. When a duplicate is found, it is
enough to calculate the length between the old and the newly found duplicate.
Rather than a set, using a dictionary whose key is the rest and value its
position in the decimal form of the fraction will solve both problem.

```python
def find_cycle(n):
    rest = 1
    seen = {}
    for i in itertools.count(0):
        if rest == 0:
            return 0
        if rest in seen:
            return i - seen[rest]

        seen[rest] = i
        rest = (rest * 10) % n
```

The last step is to test all numbers below 1000 and find the one with the
greatest cycle.

```python
def reciprocal_cycles(n=1000):
    return max(((find_cycle(i), i) for i in range(2, n)))[1]
```