# Modulus reduction

The [Brute force](./solution1.md) approach only works thanks to Python's infinite precision integers.
In other languages, the result of \\( 1000^{1000} \\) is too large to be stored in an integer.

Thus, the need of a [modulus exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation#Direct_method) algorithm, which exploits the property that \\(a \times b \pmod{m} = [(a \pmod{m}) \times (b \pmod{m})] \pmod{m} \\) for any \\( m \\).
Although modulus exponentiation may involve more multiplications than exponentiation followed by modulus, because optimized exponentiation algorithms are better than \\( O(n) \\).
In modulus exponentiation the base is always bound by \\( m \\), leading to smaller exponentiation and faster computation overall.
Consequently, this method reduce both the memory usage, which make it suitable for other languages, and the computation time.

The use of [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce) eliminates the need for a loop and is a more efficient and elegant solution.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0048/solution2.py):

```python
def mod_pow(b, e, mod):
    return reduce(lambda acc, _: (acc * b) % mod, range(e), 1)
```

Similarly, the cumulative sum can also be computed using [functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0048/solution2.py):

```python
def self_powers():
    mod = 10**10
    sums = (mod_pow(i, i, mod) for i in range(1, 1001))
    return reduce(lambda acc, y: (acc + y) % mod, sums)
```

It is worth mentioning that there exists many optimized techniques for [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method) which can be implemented.
