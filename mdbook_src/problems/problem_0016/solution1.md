# Brute force

Thanks to python, the solution is trivial, we just need to sum the digits of a
number, which can be done by casting it into a string and iterating on it.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0016/solution1.py):

```python
def power_digit_sum(n=1000):
    return sum((int(d) for d in str(2**n)))
```
