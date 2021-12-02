# Brute force

Finding number that can be written as the sum of fifth powers of theirs digits
is easy. The main difficulty of this problem is to find an upper bound and thus
to know when to stop the iteration.

The sum of the fifth powers of a \\( n \\)-digits number will always be less
than or equal to \\( n * 9^5 \\). We need to find \\( n \\) such that \\( n *
9^5 < 10^n - 1 \\) for all \\( n \\). The solution is actually very complex, but
with \\( n = 5 \\) we have \\( 5 * 9^5 = 295245 > 10^5 - 1 \\) and with \\( n =
6 \\) we have \\( 6 * 9^5 = 354294 < 10^6 - 1 \\). Which implies that it is
pointless to try any number with more than 6 digits.

```python
def digit_fifth_powers():
    return sum((n for n in range(2, 999999)
                if sum(int(i) ** 5 for i in str(n)) == n))
```