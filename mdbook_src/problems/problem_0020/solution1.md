# Brute force

As always, problems involving large numbers are easy to solve in Python, just
compute the number and iterate on it as a string:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0020/solution1.py):

```python
def factorial_digit_sum(n=100):
    return sum(int(x) for x in str(factorial(n)))
```
