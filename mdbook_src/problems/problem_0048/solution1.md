# Brute force

The naive approach consists of computing the sum of the series and then take the last 10 digits.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0048/solution1.py):

```python
def self_powers():
    return sum(i**i for i in range(1, 1001)) % 10**10
```
