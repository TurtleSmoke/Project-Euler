# Brute force

A direct approach to determine all distinct values of \\( \displaystyle \binom n r \leq 1000000 \\) for \\( 1 \le n \le 100 \\) is as follows:

- Calculate \\( \displaystyle \binom n r \\) using the formula \\( \displaystyle \binom n r = \dfrac{n!}{r!(n-r)!} \\).
- Iterate over each \\( n \\) from \\( 1 \\) to \\( 100 \\) and \\( r \\) from \\( 1 \\) to \\( n \\) and count the number of \\( \displaystyle \binom n r > 1,000,000 \\).

The first task can be simply implemented using the [math.factorial](https://docs.python.org/3/library/math.html#math.factorial) function.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0053/solution1.py):

```python
def ncr(n, r):
    return int((factorial(n) / (factorial(r) * factorial(n - r))))
```

The solution is then simpy implemented by iterating over all \\( n \\) and \\( r \\) and counting the number of \\( \displaystyle \binom n r \\) that are greater than \\( 1,000,000 \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0053/solution1.py):

```python
def combinatoric_selections():
    return sum(ncr(n, r) > 1000000 for n in range(23, 101) for r in range(1, n))
```
