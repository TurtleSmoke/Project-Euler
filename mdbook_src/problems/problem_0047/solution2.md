# Cache is life

A clear strategy to enhance the [Brute force](./solution1.md) approach is to cache some results.
At each iteration, only the prime decomposition of the current number needs to be computed.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0047/solution2.py):

```python
def distinct_primes_factors():
    cache = [False] * 4
    for i in itertools.count(1):
        cache[i % 4] = len(set(primefactors(i))) == 4
        if all(cache):
            return i - 3
```
