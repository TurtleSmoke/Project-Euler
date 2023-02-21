# Brute force

To identify curious numbers, we first need to iterate over each digit of the number and calculate the factorial of each digit.
Then, we need to sum all the factorials and compare the result with the original number.
If the sum is equal to the original number, then we have found a curious number.

To speed up the process, we can precompute the factorials and iterate over all digits using Python's string.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0034/solution1.py):

```python
def is_criterion(x):
    facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return x == sum(facts[int(i)] for i in str(x))
```

The next step is to iterate over all numbers and find curious numbers, but we need to find an upper bound.
If we take a number \\( x \\) with \\( d \\) digits, we have \\( 10^{d-1} \leq x < 10^d \\).
If \\( x \\) is the equal to the sum of factorials of its digits, then with \\( x_i \\) being the ith digit of \\( x \\), we have \\( x = \sum_{i=1}^d x_i! < d * 9! \\).

Thus, we have \\( 10^{d-1} \leq x < d * 9! \\). With d=8, the equation is wrong. Therefore, our upper bound is \\( 7 * 9!\\).

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0034/solution1.py):

```python
def digit_factorials():
    return sum(i for i in range(3, 7 * 362880) if is_criterion(i))
```
