# Brute force

The problem is to find the sum of the set of six cyclic 4-digit numbers for which each polygonal type is represented by a cyclic number in the set.
To resume, this problem has 3 constraints:

1. The numbers are 4-digit numbers.
2. The numbers are cyclic.
3. Each number is a polygon of a given type.

The brute force solution for this problem, while simple, is not easy to implement due to its recursive nature.

The idea is to try every 4-digit number until a polygon is found.
Starting with the last two digits of the previous polygon, this operation should be repeated 5 times.
If all polygon types have been found, and the last two digits of the last polygon are the same as the first two digits of the first polygon, the solution is the sum of this cycle.

Overall, the recursive algorithm requires to keep track of the remaining polygon types, the current number, and the current cycle.
The remaining polygon types is represented with a list of functions that return whether a number is a polygon.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0061/solution1.py):

```python
def find_cycle(first_two_digits, is_polygonals, cycle):
    if not is_polygonals:
        if cycle[0] // 100 == cycle[-1] % 100:
            return cycle
        return []

    for last_two_digits in range(10, 100):
        p = first_two_digits * 100 + last_two_digits
        for i, is_polygonal in enumerate(is_polygonals):
            if is_polygonal(p):
                new_cycle = find_cycle(last_two_digits, is_polygonals[:i] + is_polygonals[i + 1 :], cycle + [p])
                if new_cycle:
                    return new_cycle

    return []
```

The rest is to actually build the list of polygon types and to call the recursive function.
The formulas for each polygon type are similar to the one in [Problem 0042](../problem_0042/problem.md), and can be found in the source code.
Therefore, they will not be repeated in this text for brevity.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0061/solution1.py):

```python
def cyclical_figurate_numbers():
    is_triangular = lambda n: ((1 + (1 + 8 * n) ** 0.5) / 2).is_integer()
    is_square = lambda n: (n**0.5).is_integer()
    is_pentagonal = lambda n: ((1 + (1 + 24 * n) ** 0.5) / 6).is_integer()
    is_hexagonal = lambda n: ((1 + (1 + 8 * n) ** 0.5) / 4).is_integer()
    is_heptagonal = lambda n: ((3 + (9 + 40 * n) ** 0.5) / 10).is_integer()
    is_octagonal = lambda n: ((1 + (1 + 3 * n) ** 0.5) / 3).is_integer()
    is_polygonals = [is_triangular, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal]

    for i in range(10, 100):
        cycle = find_cycle(i, is_polygonals, [])
        if cycle:
            return sum(cycle)

    return []
```
