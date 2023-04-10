# Brute force

The problem is to determine the number of positive integers that are nth power.
Here, positive integers refer to integers greater than 0.

The brute force algorithm for solving this problem is relatively straightforward:

1. Iterate through all positive integers.
2. For each integer, iterate through all positive powers.
3. If the length of the computer number is equal to the power, increment the counter.

However, the challenge lies in determining when to terminate both iterations.

To express the problem mathematically, we search all \\( n \\) and \\( x \\) such that \\( 10^{n-1} \leq x^n < 10^n \\).
It follows that \\( x \\) must be less than \\( 10 \\), and \\( 10^{n-1} \\) grows faster than \\( x^n \\) since \\( x < 10 \\).
Therefore, the iteration over \\( n \\) can be stopped when \\( 10^{n-1} > x^n \\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0063/solution1.py):

```python
def powerful_digit_counts():
    res = 0
    for i in range(1, 10):
        for j in itertools.count(1):
            if len(str(i**j)) == j:
                res += 1
            elif len(str(i**j)) < j:
                break
    return res
```

