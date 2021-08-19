# Brute force

As always, the brute force solution is quite simple, first determine if a number
is evenly divisible by all numbers from 1 to 20.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0005/solution1.py):

```python
def is_evenly_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True
```

Then iterate until you find a solution.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0005/solution1.py):

```python
def smallest_multiple():
    i = 1
    while not is_evenly_divisible(i):
        i += 1
    return i
```
