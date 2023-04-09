# Iterating and caching

The main issue with the [Brute force](./solution1.md) approach is that it checks the same permutations multiples times and many of them are not cubes, making it very inefficient.

To overcome this issue, we can use a similar approach to [Problem 0049](../problem_0049/problem.md) which involves:
1. Generating all cubes \\( n^3 \\).
2. Grouping the cubes with the same permutation together.
3. If one of the groups has at least \\( 5 \\) cubes, the solution is found.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0062/solution2.py):

```python
def cubic_permutations():
    permutations = defaultdict(list)
    for cube in (i**3 for i in itertools.count(1)):  # Condition 1
        ordered_digits = "".join(sorted(str(cube)))
        permutations[ordered_digits].append(cube)  # Condition 2
        if len(permutations[ordered_digits]) >= 5:  # Condition 3
            return min(permutations[ordered_digits])
```

Note that the function actually returns the smallest cube of the first group with at least \\( 5 \\) cubes.
While this is sufficient for this problem, it will not necessarily provide the correct answer with groups of bigger sizes, like \\( 6 \\).