# Caching polygonal numbers

Instead of iterating through all 4-digit numbers, pre-computing all polygonal numbers and then iterating through them is a better approach.

It does not change the `find_cycle` function by much, instead of trying every 4-digit number, it tries every polygonal number.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0061/solution2.py):

```python
def find_cycle(first_two_digits, polygonals, cycle):
    if not polygonals:
        if cycle[0] // 100 == cycle[-1] % 100:
            return cycle
        return []

    for i in range(len(polygonals)):
        for p in polygonals[i]:
            if p // 100 == first_two_digits:
                new_cycle = find_cycle(p % 100, polygonals[:i] + polygonals[i + 1 :], cycle + [p])
                if new_cycle:
                    return new_cycle

    return []
```

The rest is also very similar, the difference is the list of polygon types which is now a list of sets of polygonal numbers and the iteration is done starting with the octogonals numbers.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0061/solution2.py):

```python
def cyclical_figurate_numbers():
    triangles = set(n * (n + 1) // 2 for n in range(45, 141))
    squares = set(n**2 for n in range(32, 100))
    pentagonals = set(n * (3 * n - 1) // 2 for n in range(26, 82))
    hexagonals = set(n * (2 * n - 1) for n in range(23, 71))
    heptagonals = set(n * (5 * n - 3) // 2 for n in range(21, 64))
    octagonals = set(n * (3 * n - 2) for n in range(19, 59))

    polygonals = [triangles, squares, pentagonals, hexagonals, heptagonals]
    for p in octagonals:
        cycle = find_cycle(p, polygonals, [p])
        if cycle:
            return sum(cycle)

    return []
```
