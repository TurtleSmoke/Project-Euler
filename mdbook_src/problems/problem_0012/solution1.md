# Brute force

Finding the number of factors of \\( n \\) can be done by iterating from 1 to
\\( n \\) and checking each number that can divide \\( n \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0012/solution1.py):

```python
def number_of_factors(n):
    res = 1
    for i in range(2, n):
        if n % i == 0:
            res += 1
    return res
```

[Triangular number](https://en.wikipedia.org/wiki/Triangular_number) can be
computed quite easily with a loop, we can generate them as long as their number
of divisor is less than \\( 500 \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0012/solution1.py):

```python
def highly_div_triangular_number(n=500):
    i = 1
    res = 1
    while number_of_factors(res) < n:
        i += 1
        res += i

    return res
```
