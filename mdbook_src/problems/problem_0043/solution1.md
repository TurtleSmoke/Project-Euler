# Brute force

The problem can be split into two parts:

- Check if the permutation satisfies the divisibility property.
- Find all the permutations of the digits \\( 0 \\) to \\( 9 \\).

The first part can be done by checking if a particular section of the number is divisible by the corresponding prime number.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0043/solution1.py):

```python
def is_sub_string_divisible(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    return all(int(str(n)[i + 1 : i + 4]) % d == 0 for i, d in enumerate(divisors))
```

The second part is done by using the [itertools.permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) function.
With the caveat that any permutation starting with \\( 0 \\) should be disregarded.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0043/solution1.py):

```python
def sub_string_divisibility():
    res = 0
    for i in itertools.permutations("9876543210"):
        if i[0] == "0":
            continue
        x = int("".join(i))
        if is_sub_string_divisible(x):
            res += x
    return res
```

It is worth noting that if we encounter a permutation beginning with \\( 0 \\), we can immediately return the result without further iterations, as all other permutations will also start with \\( 0 \\).