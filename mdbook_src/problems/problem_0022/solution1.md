# Brute force

We first get the huge list of names in python, we just need to remove the `""`
around them.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0022/read_file.py):

```python
def read_file(filename):
    with open(filename, 'r') as file:
        return [name[1:-1] for name in file.read().split(",")]
```

Then we just need to sum the letters of the names by their position in the
alphabet. Since all the names are capitalized, we can remove `ord('A') + 1` to
get their position in the alphabet. The last step is to sum the position of the
names in the list by its value.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0022/solution1.py):

```python
def names_scores(filename):
    names = read_file(filename).sort()
    return sum((i + 1) * sum(ord(c) - ord('A') + 1 for c in name)
               for (i, name) in enumerate(names))
```
