# Brute force

Computing the sum of digits of a number is a task that we already know.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0056/solution1.py):

```python
def digits_sum(n):
    return sum(map(int, str(n)))
```

Then, we can solve the problem by iterating over all the possible values of a and b, and keeping track of the maximum sum.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0056/solution1.py):

```python
def powerful_digit_sum():
    return max(digits_sum(a**b) for a in range(1, 100) for b in range(1, 100))
```
