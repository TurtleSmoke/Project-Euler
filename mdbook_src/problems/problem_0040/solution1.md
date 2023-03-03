# Brute force

The [Champernowne constant](https://en.wikipedia.org/wiki/Champernowne_constant) is a number obtained by concatenating positive integers in decimal form.
The simplest way to solve this problem is to create a string with the required 1000000 digits and then extract the ones we need.

In Python, we can use the built-in [join](https://docs.python.org/3/library/stdtypes.html#str.join) method to construct this string easily.
This function creates a string which is the concatenation of an iterable ; a range of integers in our case.

The final result is the product of the digits we need.
Combining the [reduce](https://docs.python.org/3/library/functools.html#functools.reduce) function from the [functools](https://docs.python.org/3/library/functools.html) module and the [int](https://docs.python.org/3/library/functions.html#int) function with [operator.mul](https://docs.python.org/3/library/operator.html#operator.mul), we can get the product of a iterable of integers.


From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0040/solution1.py):

```python
def champernownes_constant():
    s = "".join(str(i) for i in range(1, 1000000))
    print([int(s[10 ** i - 1]) for i in range(7)])
    return reduce(operator.mul, (int(s[10 ** i - 1]) for i in range(7)))
```
