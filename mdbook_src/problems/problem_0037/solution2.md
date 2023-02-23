# Construct them all

The [Brute force](./solution1.md) solution stops when the eleven primes are found.
This is not a very efficient solution. Instead, we can construct all the truncatable primes.

The first digit must be 2, 3, 5 or 7 because the left slice will leave that digit at the end.
For the same reason, the last digit must be 2, 3, 5 or 7.
Since our solution must have at least 2 digits, the last digit cannot end with 2 or 5, as the right slice will leave a multiple of 2 or 5 at the end.

So the first digit is either 2, 3, 5 or 7 and the last digit is either 3 or 7.

The process is recursive. We will append numbers to the right.
It is only possible to add 1, 3, 7 or 9 to the right. In this case we can use 1 or 9 because if it ends in the middle of a number, it won't be a single digit with left or right truncating.
Obviously, the number will not be a truncatable prime, but the next iterations might be.

If the number is not a prime, there is no point to continue the recursion.
Indeed, if we continue, the right-truncating will end on this number, which is not prime and thus not truncatable.
On the contrary, the recursion can be continued until the number is not prime.

By construction, the number is prime and right-truncatable.
As explained before, we need to check if it is left-truncatable only if the number ends with 3 or 7.
If so, we can add it to the list of truncatable primes.

We will use the keyword [yield](https://docs.python.org/3/reference/simple_stmts.html#yield) and [yield from](https://docs.python.org/3/reference/simple_stmts.html#yield) to return the results as we find them.
The `yield from` statement is similar to the `yield` statement, but it is used to return the results of a generator function.
In a nutshell, we just have to use the [sum](https://docs.python.org/3/library/functions.html#sum) builtin on the returned values.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0037/solution2.py):

```python
def construct_truncatable_primes(num):
    if isprime(num):
        if num > 10 and num % 10 in (3, 7) and is_left_truncatable(str(num)):
            yield num
        for new_digit in (1, 3, 7, 9):
            yield from construct_truncatable_primes(num * 10 + new_digit)
```

The final solution is just the sum of all the constructed truncatable primes starting with 2, 3, 5 and 7.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0037/solution2.py):

```python
def truncatable_primes():
    return sum(sum(construct_truncatable_primes(d)) for d in (2, 3, 5, 7))
```
