# Brute force

The brute force solution is simple, just iterate until the number of digits 
is at least 1000. We can count the number of digits in a number by turning 
it into a string and counting its length.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0025/solution1.py):

```python
def thousandth_digit_fibonacci_number(n=1000):
    f1 = 1
    f2 = 1
    res = 1
    while len(str(f1)) < n:
        f1, f2 = f2, f1 + f2
        res += 1

    return res
```
