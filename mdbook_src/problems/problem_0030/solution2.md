# Search unique combination

There is no need to try all numbers with at most 6 digits. What is really
important is to try all combinations of numbers with at most 6 digits. For
example, the sum of the fourth powers of digits of \\( 1346 \\) is the same as
the sum of \\( 1634, 1436\dots \\) But even if the sum is the same for \\(
1356 \\) and \\( 1634 \\), only \\( 1634 \\) has a sum equal to itself. So how
can we avoid calculating duplicate combinations but still find the solution ?

We need to build a list of these combinations, which is easily done with a
recursive function. The idea is to create the string so that the digits are
sorted. The stopping condition is the number of digits. Recursive functions are
a pain to understand, but if you print the result and the string after each
iteration, you should understand the function without too much trouble.

I used `yield` instead of building an entire list, but you can consider that
it's the same thing.

```python
def build_combination(d, n=0, s=''):
    if d == 0:
        yield s
    else:
        for i in range(n, 10):
            for v in build_combination(d - 1, i, s + str(i)):
                yield v

```

The trick is to compute the sum a first time, for example, taking \\( 1346 \\)
which sum is equal to \\( 1^5 + 3^5 + 4^5 + 6^5 = 1634 \\). Then, repeat the
operation a second time \\( 1^5 + 6^5 + 3^5 + 4^5 = 1634 \\). If the total is
the same for both computations, then you have found one combination that works.

Instead of computing the fifth power of each digit, we can compute them once and
store them in a cache. The rest is just trying all the previously found
combinations. We need to remove `1` from the final result as the problem
indicates.

```python
def digit_fifth_powers():
    cache = [i ** 5 for i in range(0, 10)]
    res = 0
    for n in build_combination(6):
        total = sum(cache[int(c)] for c in n)
        if sum(cache[int(c)] for c in str(total)) == total:
            res += total

    return res - 1
```
