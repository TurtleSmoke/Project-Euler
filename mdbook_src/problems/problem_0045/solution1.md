# Brute force

The brute force approach for solving this problem is straightforward.
To start, a function is needed to compute \\( T_n \\), \\( P_n \\) and \\( H_n \\) for a given \\( n \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution1.py):

```python
def tn(n):
    return n * (n + 1) // 2
```

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution1.py):

```python
def pn(n):
    return n * (3 * n - 1) // 2
```

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution1.py):

```python
def hn(n):
    return n * (2 * n - 1)
```

Then, a while loop can be implemented to iterate until all three numbers are equal.
At each iteration, only update one of the two smallest value among \\( T_n \\), \\( P_n \\) and \\( H_n \\).
This is because \\( T_n \\), \\( P_n \\) and \\( H_n \\) are all increasing functions of \\( n \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0045/solution1.py):

```python
def triangular_pentagonal_and_hexagonal():
    t, p, h = 286, 166, 144
    ti, pi, hi = tn(t), pn(p), hn(h)
    while not (ti == pi == hi):
        if ti < pi:
            t += 1
            ti = tn(t)
        elif pi < hi:
            p += 1
            pi = pn(p)
        else:
            h += 1
            hi = hn(h)
    return ti
```
