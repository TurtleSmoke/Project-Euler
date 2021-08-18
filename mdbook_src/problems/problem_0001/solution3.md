# Summing everything

The [Three by three](solution2.md) solution is quite interesting because it
reduces the problem into smaller parts. For example, the sum of multiples of
three is the following:

\\[ 3 + 6 + 9 + 12 + 15 + ... \\]
\\[ 3 * ( 1 + 2 + 3 + 4 + 5 ...) \\]
\\[ 3 * \sum_{i=0}^{\lfloor\frac{1000}{3}\rfloor} x_i \\]

It is the sum of an arithmetic sequences, which is equal to:

\\[ \frac{n*(n+1)}{2} \\]

The [Three by three](solution2.md) solution can be reduced to:

\\[ 3 * \frac{\lfloor\frac{999}{3}\rfloor * (\lfloor\frac{999}{3}\rfloor + 1)}{2} +5 * \frac{\lfloor\frac{999}{5}\rfloor * (\lfloor\frac{999}{5}\rfloor + 1)}{2} -15 * \frac{\lfloor\frac{999}{15}\rfloor * (\lfloor\frac{999}{15}\rfloor + 1)}{2} \\]

Note that the limit is 999 because 1000 should not be included.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0001/solution3.py):

```python
def sum_of_three_and_five(limit=999):
    limit_3 = limit // 3
    limit_5 = limit // 5
    limit_15 = limit // 15

    sum_3 = 3 * (limit_3 * (limit_3 + 1) // 2)
    sum_5 = 5 * (limit_5 * (limit_5 + 1) // 2)
    sum_15 = 15 * (limit_15 * (limit_15 + 1) // 2)

    return sum_3 + sum_5 - sum_15
```
