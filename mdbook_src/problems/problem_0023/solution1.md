# Brute force

We are searching for all numbers that are **not** the sum of two abundant
numbers. Since every integer larger than 28123 can be written as the sum of two
abundant numbers, our upper limit is therefore 28123.

First, we need to find all the abundant number below 28123, going higher is
pointless because we are searching for positive numbers only. An abundant number
is a number that have a larger sum of divisors than itself. We already have a
function to compute the sum of divisors, we just need to be aware that if \\(
\sqrt{n} \\) divide \\( n \\), it only has to count once.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution1.py):

```python
def sum_of_factors(n):
    res = 1
    root = floor(sqrt(n))
    for i in range(2, root + 1):
        if n % i == 0:
            res += i + n // i

    if root**2 == n:
        res -= root

    return res
```

We just need to check if a number is the sum of two of the abundant numbers
calculated earlier. The naive way to do this is to try every combination of two
abundant numbers.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution1.py):

```python
def is_sum(i, abundant):
    return any(a1 + a2 == i for a1 in abundant for a2 in abundant)
```

Finally, we just have to sum each number less than 28124 that is not the sum 
of two abundant numbers.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution1.py):

```python
def non_abundant_sums():
    abundant = [i for i in range(1, 28124) if sum_of_factors(i) > i]

    return sum(i for i in range(28124) if not is_sum(i, abundant))
```
