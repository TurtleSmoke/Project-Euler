# Tree of primitive Pythagorean triples

The objective is to determine the number of Pythagorean triples that yield a unique perimeter.

Thanks to [Problem 0039](../problem_0039/problem.md), the process of computing all pythagorean triples becomes straightforward

We can actually use the code in the [Tree of primitive Pythagorean triples](../problem_0039/solution4.md) solution.
However, we need to replace the return statement in order to count the number of perimeter that can only be formed in one possible way.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0075/solution1.py):

```python
def compute_all_pythagorean_triples(results, max_p, abc):
    curr_p = sum(abc)
    if curr_p < max_p:
        for perimeter in range(curr_p, max_p, curr_p):
            results[perimeter] += 1
        compute_all_pythagorean_triples(results, max_p, A @ abc)
        compute_all_pythagorean_triples(results, max_p, B @ abc)
        compute_all_pythagorean_triples(results, max_p, C @ abc)
```

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0075/solution1.py):

```python
def singular_integer_right_triangles():
    results = defaultdict(int)
    compute_all_pythagorean_triples(results, 1500000, np.array([3, 4, 5]))
    return sum(filter(lambda x: x == 1, results.values()))
```
