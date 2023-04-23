# Caching totients

The current [Brute force](./solution1.md) solution is inefficient due to its bottleneck is the computation of \\( \phi(n) \\).
The function `are_coprime` is called \\( n \\) times, and each call takes \\( O(n) \\) time, leading to a total runtime of \\( O(n^3) \\) for all \\( \phi(n) \\).

A more efficient solution involves using a similar process to the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), where every multiple of a \\( a \leq n \\) is not coprime to \\( n \\).
By employing this method, \\( \phi(n) \\) for all \\( n \\) can be computed in \\( O(n \log(\log(n))) \\) time.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0069/solution2.py):

```python
def totient_list(n):
    tlist = list(range(n))
    for i in range(1, n):
        p = tlist[i]
        for j in range(2 * i, n, i):
            tlist[j] -= p
    return tlist
```

Furthermore, caching all totients enables the computation of \\( \frac{n}{\phi(n)} \\) for all \\( n \\) in linear time.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0069/solution2.py):

```python
def totient_maximum(limit=1000001):
    res = 0
    res_n = 0
    totatives = totient_list(limit)
    for n in range(2, limit):
        if n / totatives[n] > res:
            res = n / totatives[n]
            res_n = n
    return res_n
```
