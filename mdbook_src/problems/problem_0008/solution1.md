# Brute force

We are searching for the largest product of 13 adjacent digits in a 1000-digit
number. We want to calculate the product of each 13 adjacent digits and find the
largest one.

The 1000-digit number will be stored in a file, so the first step is to get this
number as a string and remove each trailing newline (\n):

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return file.read().replace("\n", "")
```

Given this string, we need to calculate the product of 13 adjacent digits, which
can be done easily
using [math.prod()](https://docs.python.org/3/library/math.html#math.prod).
Then, simply repeat this step for all 13 adjacent digits contained in the
1000-digit number and save the maximum of these products.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution1.py):

```python
def largest_product_in_series(n, adj=13):
    res = 0
    for i in range(len(n) - adj):
        res = max(prod(int(digit) for digit in n[i : i + adj]), res)

    return res
```
