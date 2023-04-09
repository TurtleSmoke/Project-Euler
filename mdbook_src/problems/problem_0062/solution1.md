# Brute force

The problem is to find the smallest cube \\( n^3 \\) such that it has at least \\( 5 \\) permutations that are also cubes.
The brute force approach is exactly what it sounds like:

1. Generate all cubes \\( n^3 \\).
2. Generate all permutations of this cube .
3. Check if the permutations are cubes with the same number of digits and is not already counted.
4. If there are \\( 5 \\) or more permutations that meet the criteria, then the solution is found

Using [itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) greatly simplifies the second step.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0062/solution1.py):

```python
def cubic_permutations():
    for cube in (i**3 for i in itertools.count(1)):  # Condition 1
        cubes = {cube}

        for p in itertools.permutations(str(cube)):  # Condition 2
            new_cube = int("".join(p))
            if p[0] != "0" and is_cube(new_cube) and new_cube not in cubes:  # Condition 3
                cubes.add(new_cube)
        if len(cubes) >= 5:  # Condition 4
            return min(cubes)
```

Although this method works for the given example, it is too slow to solve the problem.
