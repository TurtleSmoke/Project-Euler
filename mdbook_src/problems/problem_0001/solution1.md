# Naive solution

The first problem is actually quite easy, the naive solution would be to iterate
over every number between 0 and 1000 and check those that are multiples of 3 or
5.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0001/solution1.py):

```python
def sum_of_three_and_five(limit=1000):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)
```