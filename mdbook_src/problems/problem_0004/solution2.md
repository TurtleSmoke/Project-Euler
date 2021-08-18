# Factorisation is the key

We know that the researched number is larger than \\( 100\*100 = 10000 \\)
and smaller than \\( 999\*999 = 998001 \\). So it must be of the form \\(
abcba \\) or \\( abccba \\). Let's assume it is of the form \\( abccba \\), if
it does not work, we'll try with \\( abcba \\).

\\( abccba = 10001a + 10010b + 1100c = 11(9091a + 910b + 100c) \\) which means
that the palindrome must be divisible by 11. Since 11 is prime, either \\(
100001a \\), \\( 10010b \\) or \\( 1100c \\) is a multiple of 11, which is why
the iteration can be done 11 by 11.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0004/solution2.py):

```python
def largest_palindrome_product():
    res = 0
    for x in range(110, 1000, 11):
        for y in range(x, 1000):
            if x * y > res and is_palindrome(x * y):
                res = x * y

    return res
```

We went from 405450 iterations with the [Brute force](solution1.md) to 36450
iterations !
