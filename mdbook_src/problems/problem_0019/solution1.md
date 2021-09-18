# Brute force

This problem is not fascinating, we could start from the first of January 1901
as a Tuesday, and iterate on each month, for example the first day of February
1901 is Tuesday + \\( 31\ \\%\ 7 \\), which is Friday. We could continue by
taking leap year into account. But thanks to Python, we can solve this problem
with a simpler solution:

From [solution1.py](https://github.com/turtlesmoke/project-euler/blob/main/problems/problem_0019/solution1.py):

```python
def counting_sundays():
    res = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                res += 1

    return res
```
