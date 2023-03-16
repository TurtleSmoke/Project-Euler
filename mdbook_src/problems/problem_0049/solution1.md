# Brute force

The brute force approach iterates over all four-digit numbers, \\( i \\), and all numbers \\( j \\) until \\( i \\), \\( i + j \\) and \\( i + 2j \\) are primes and permutations of each other.
The requirement for the four-digit numbers implies that \\(1000 \leq i < 10000 \\) and \\( i + 2j < 10000 \Rightarrow j < \frac{10000 - i}{2} \\).

The permutations condition can be verified by sorting the digits of each number and comparing the sorted strings.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0049/solution1.py):

```python
def prime_permutations():
    for i in range(1000, 10000):
        if i == 1487:
            continue
        for j in range(1, (10000 - i) // 2):
            if (
                isprime(i)
                and isprime(i + j)
                and isprime(i + 2 * j)
                and sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + 2 * j))
            ):
                return str(i) + str(i + j) + str(i + 2 * j)
```
