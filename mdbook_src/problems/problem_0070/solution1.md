# Brute force

The problem is very similar to the [Problem 0069](../problem_0069/problem.md) as it also involves Euler's totient function.
This problem asks to find the value of \\( n \\) for which \\( \frac{n}{\phi(n)} \\) is minimal and \\( n \\) is a permutation of \\( \phi(n) \\).

Thanks to the [Problem 0069](../problem_0069/solution1.md), generating a list of totients is easy.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0070/solution1.py):

```python
def totient_list(n):
    tlist = list(range(n))
    for i in range(1, n):
        p = tlist[i]
        for j in range(2 * i, n, i):
            tlist[j] -= p
    return tlist
```

Therefore, filtering every totient that is not a permutation of its index and finding the minimum ratio is all that is left to do.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0070/solution1.py):

```python
def totient_permutation(limit=10000001):
    totatives = totient_list(limit)
    totatives = ((n, t) for n, t in enumerate(totatives) if sorted(str(n)) == sorted(str(t)) and n > 1)
    return min(totatives, key=lambda x: x[0] / x[1])[0]
```
