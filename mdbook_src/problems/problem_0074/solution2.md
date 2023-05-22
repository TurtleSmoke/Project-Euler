# Caching the chain

The main drawback of the [Brute force](./solution1.md) approach is that it recalculates the whole chain for each number.
One way to improve the performance is to cache the length of the chain for each number of the chain.

This approach use a dictionary to store the chain length for each number.
Instead of using a set, a list is preferred to keep track of the position of each number in the chain.
For each number below one million, the chain is computed as before.
However, if the current number already exists in the dictionary, indicating that its length is already known, the computation can be terminated prematurely.

Upon completion of the chain, every number in the current chain is added to the dictionary.
The value assigned to each number is equal to its position in the chain plus the length of the final element in the chain.
If the final element is not present in the dictionary, its length is set to zero.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0074/solution2.py):

```python
def digit_factorial_chains():
    res = 0
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    cache = {}
    for i in range(1, 1000000):
        found = []
        while i not in found and i not in cache:
            found.append(i)
            i = sum([factorials[int(digit)] for digit in str(i)])
        for j, v in enumerate(found):
            cache[v] = len(found) - j + cache.get(i, 0)
            if cache[v] == 60:
                res += 1
    return res
```
