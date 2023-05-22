# Brute force

The objective is to determine the number of chains with a starting number below one million that consist of exactly sixty non-repeating terms.

A straightforward approach is to iterate through each number below one million, calculate the chain using a set to track the terms already seen, and increment the count if the chain has exactly sixty terms.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0074/solution1.py):

```python
def digit_factorial_chains():
    res = 0
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    for i in range(1, 1000000):
        found = set()
        while i not in found:
            found.add(i)
            i = sum([factorials[int(digit)] for digit in str(i)])
        if len(found) == 60:
            res += 1
    return res
```
