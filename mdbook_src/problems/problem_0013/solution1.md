# Brute force

The main problem is to find a way to add large numbers, because computers can
not store large numbers so easily. That's the point of the problem, to find a
way to add those numbers. We could use an array to store each digit of each
number and add them, but thanks to python and
the [unifying long integers and integers](https://www.python.org/dev/peps/pep-0237/)
we can just add these numbers without worrying about memory.

We just need to get the first 10 digits of the additions, which can be done
quite easily by converting the number to a string ang get the first 10
characters.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0013/solution1.py):

```python
def large_sum(filename):
    return str(sum(read_file(filename)))[:10]
```
