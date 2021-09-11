# Brute force

Calculating the number of iterations of the Collatz sequence is easy, just
follow the sequence until it reaches one, and count the number of iterations
to get there:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0014/solution1.py):

```python
def collatz(n):
    iteration = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        iteration += 1

    return iteration
```

Then, just check the iteration for each starting number from 1 to 1000000 and
return the largest.

From [solution1.py](https://github.com/turtlesmoke/project-euler/blob/main/problems/problem_0014/solution1.py):

```python
def longest_collatz_sequence(n=1000000):
    res, max_it = 0, 0
    for i in range(1, n):
        current_it = collatz(i)
        if current_it > max_it:
            res, max_it = i, current_it

    return res
```
