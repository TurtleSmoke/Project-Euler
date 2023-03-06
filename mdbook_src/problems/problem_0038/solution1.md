# Brute force

I choose to take one number as a seed, and detect if the product of this seed can form a pandigital number.
To do this, you multiply the seed number by increasing numbers until the resulting number is either greater than 9 digits or a pandigital number.
Python's string functions make it easy to concatenate numbers, and a set is used to check if a number is pandigital.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0038/solution1.py):

```python
def is_pandigital_multiples(seed):
    digits = str(seed)
    for j in itertools.count(2):
        digits += str(seed * j)
        if len(digits) > 9:
            return -1
        if len(digits) == 9 and set(digits) == set("123456789"):
            return int(digits)
```

The maximum value for the seed is 10000 because if we multiply 10000 by 1 and 2 and concatenate the results, we get a 10-digit number, which cannot be pandigital.
The solution is then given by iterating over every seed and returning the maximum pandigital number found.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0038/solution1.py):

```python
def pandigital_multiples():
    return max(is_pandigital_multiples(seed) for seed in range(1, 10000))
```
