# 0 are useless

The problem requires calculating a product, a product of something and 0 will
always give a result of 0. Which means that every 13 adjacent digits containing
0 are useless since the result will never be the largest product.

The 1000-digit number can actually be split around each 0, of course if a number
has less than 13 digits it can be deleted.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution2.py):

```python
def split_series(n):
    return [sub_n for sub_n in n.split("0") if len(sub_n) >= 13]
```

Another improvement reside in not calculating every product from the start, for
example if we search the product of 3 adjacent digits in 12345, the 3 solutions
are:

```python
1*2*3     = 6
  2*3*4   = (6 / 1) * 4 = 24
    3*4*5 = (24 / 3) * 5 = 60
```

The second product is the same as the first, just divide the digit that is not
present and multiply the one that is. We have to be careful with the digit 0
because division by 0 is an error, but we have already solved the problem just
before, so we can assume our number will never contain the digit 0.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution2.py):

```python
def largest_product_in_series(n, adj=13):
    res = 0
    current = prod(int(digit) for digit in n[0:adj])
    for i in range(len(n) - adj):
        current = (current // int(n[i])) * int(n[i + adj])
        res = max(res, current)

    return res
```

We simply repeat this step for each sub-number of the 1000-digit split around 0.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0008/solution2.py):

```python
def largest_product_in_multiples_series(sub_n, adj=13):
    res = 0
    for n in sub_n:
        res = max(largest_product_in_series(n, adj), res)
    return res
```
