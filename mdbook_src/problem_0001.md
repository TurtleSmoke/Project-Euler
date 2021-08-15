# [Multiples of 3 and 5](https://projecteuler.net/problem=1)

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we
> get 3, 5, 6 and 9. The sum of these multiples is 23.

> Find the sum of all the multiples of 3 or 5 below 1000.

## Naive solution

The first problem is actually quite easy, the naive solution would be to iterate
over every number between 0 and 1000 and check those that are multiples of 3 
or 5.

From [solution1.py](../problems/problem_0001/solution1.py):

```python
def sum_of_three_and_five(limit=1000):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)
```

## Better solution

The [naive solution](#naive-solution) is actually quite slow, at least it would
be if the limit was greater than 1000. Since only multiples of 3 and 5 are
needed, iterating 3 by 3 and then 5 by 5 might be faster. We have to be careful
with numbers that are multiples of 3 and 5 because they will be counted twice.
Just delete them, which is the same as removing all the multiples of 15.

From [solution2.py](../problems/problem_0001/solution2.py):

```python
def sum_of_three_and_five(limit=1000):
    sum_3 = sum(i for i in range(0, limit, 3) if i % 3 == 0)
    sum_5 = sum(i for i in range(0, limit, 5) if i % 5 == 0)
    sum_15 = sum(i for i in range(0, limit, 15) if i % 15 == 0)
    return sum_3 + sum_5 - sum_15
```

## Mathematical solution

The [better solution](#better-solution) is quite interesting because it reduces
the problem in smaller part. For the case of 3 the sum is:

\\[ 3 + 6 + 9 + 12 + 15 + ... \\]
\\[ 3 * ( 1 + 2 + 3 + 4 + 5 ...) \\]
\\[ 3 * \sum_{i=0}^{\lfloor\frac{1000}{3}\rfloor} x_i \\]

It is the sum of an arithmetic sequences, which is equal to
\\[ \frac{n*(n+1)}{2} \\]
The [better solution](#better-solution) can be reduced to:

\\[
3 * \frac{\lfloor\frac{999}{3}\rfloor * (\lfloor\frac{999}{3}\rfloor + 1)}{2} 
+5 * \frac{\lfloor\frac{999}{5}\rfloor * (\lfloor\frac{999}{5}\rfloor + 1)}{2} 
-15 * \frac{\lfloor\frac{999}{15}\rfloor * (\lfloor\frac{999}{15}\rfloor + 1)}{2}
\\]

Note that the limit is 999 because 1000 should not be included.

From [solution3.py](../problems/problem_0001/solution3.py):

```python
def sum_of_three_and_five(limit=999):
    limit_3 = limit // 3
    limit_5 = limit // 5
    limit_15 = limit // 15

    sum_3 = 3 * (limit_3 * (limit_3 + 1) // 2)
    sum_5 = 5 * (limit_5 * (limit_5 + 1) // 2)
    sum_15 = 15 * (limit_15 * (limit_15 + 1) // 2)

    return sum_3 + sum_5 - sum_15
```

## Solution
> 233168
