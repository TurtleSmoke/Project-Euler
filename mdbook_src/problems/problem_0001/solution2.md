# Three by three

The [Brute force](solution1.md) is actually quite slow, at least it would be if
the limit was greater than 1000. Since only multiples of 3 and 5 are useful,
iterating 3 by 3 and then 5 by 5 will be faster. We have to be careful with the
multiples of 3 and 5 because they will be counted twice. So we have to subtract
them from the result.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0001/solution2.py):

```python
def sum_of_three_and_five(limit=1000):
    sum_3 = sum(i for i in range(0, limit, 3) if i % 3 == 0)
    sum_5 = sum(i for i in range(0, limit, 5) if i % 5 == 0)
    sum_15 = sum(i for i in range(0, limit, 15) if i % 15 == 0)
    return sum_3 + sum_5 - sum_15
```
