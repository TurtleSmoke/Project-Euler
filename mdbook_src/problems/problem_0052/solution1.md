# Brute force

The brute force approach for this problem is very simple, as the task of identifying numbers sharing the same digit has already been solved in the [Prime permutations](../problem_0049/problem.md) problem with the [Brute force](../problem_0049/solution1.md) approach.

The remaining step consist of iterating through all positive numbers until all products wth number from 2 to 6 are permutations of the original integer.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0052/solution1.py):

```python
def permuted_multiples():
    for i in itertools.count(1):
        if all(sorted(str(i)) == sorted(str(i * j)) for j in range(2, 7)):
            return i
```
