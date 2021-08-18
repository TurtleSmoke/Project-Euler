# Brute force

> The [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) form
> a sequence, called the Fibonacci
> [sequence](https://en.wikipedia.org/wiki/Integer_sequence), such that each
> number is the sum of the two preceding ones, starting from 0 and 1.

The sum of all even numbers in the Fibonacci sequence less than 4 million can be
calculated quite easily by iterating over the sequence until the threshold is
reached by adding each even number to the result.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0002/solution1.py):

```python
def sum_of_even_fibonacci_numbers(limit=4000000):
    f0 = 1
    f1 = 2
    res = 0
    while f0 < limit:
        if f0 % 2 == 0:
            res += f0
        f0, f1 = f1, f0 + f1
    return res
```
