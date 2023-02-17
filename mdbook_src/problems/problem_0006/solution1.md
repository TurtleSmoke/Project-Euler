# Brute force

Finding the difference between the sum of the squares and the square of the sum
required two steps:

Find the sum of the squares:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0006/solution1.py):

```python
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))
```

And the square of the sum:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0006/solution1.py):

```python
def square_of_sum(n):
    return sum(i for i in range(1, n + 1)) ** 2
```

Finally, just subtract the square of the sum by the sum of the squares:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0006/solution1.py):

```python
def sum_square_difference(n=100):
    return square_of_sum(n) - sum_of_squares(n)
```
