# Brute force

The problem requires to find the number of Lychrel numbers below 10,000.
A Lychrel number is a natural number that cannot become a palindrome through the process of iteratively reversing the number and adding it to the original number.
In this problem, a number is considered a Lychrel number if fails to form a palindrome within 1 to 50 iterations.

The first step is to write a function that checks if a number is a Lychrel number.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0055/solution1.py):

```python
def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True
```

Then, iterating through all numbers below 10000 and checking is enough to solve the problem.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0055/solution1.py):

```python
def lychrel_numbers():
    return sum(is_lychrel(n) for n in range(1, 10000))
```
