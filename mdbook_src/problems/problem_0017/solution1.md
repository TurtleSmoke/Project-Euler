# Brute force

This problem is boring, there is nothing interesting to do, we can only count
some word several times. For example, the word "hundred" is used 900 times from
100 to 999, this allows some factoring. We can do the same for the number from 1
to 9, for "and", for 10, 20, 30, ...

From [solution17.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_00017/solution17.py):

```python
def number_letter_counts():
    unit = len("onetwothreefourfivesixseveneightnine")
    ten = len("teneleventwelvethirfourfifsixseveneighnine") + len("ten") * 7
    and_l = len("and")
    twenty = len("twentythirtyfortyfiftysixtyseventyeightyninety")
    hun = len("hundred")
    thou = len("onethousand")
    return thou + 900 * hun + 190 * unit + 100 * twenty + 891 * and_l + 10 * ten
```
