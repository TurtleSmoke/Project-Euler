# Maths permutations

If you have understood how lexicographic permutation are constructed, you should
have noticed that permutations are made from right to left. Before updating the
number on the left, all permutations on the right must have been made. That is
why with the string '0123', the first 6 permutations begin with '0', then the 6
following permutations with '1', and so on.

The string in our examples contains 4 characters, it implies that every \\( \( 4
\- 1 \)! \\) permutations the first digit will change. We can even tell which
one will be placed first by knowing the multipliers of that factorial. If it is
the \\( 3 \* 3! \\)th permutations, the first digit will be the third one in the
string, '3' in this example.

Since this process is recursive, we can find the first digit each time by
reducing the n-th permutations we are looking for.

For example, if we researched the 15th lexicographic permutations, we know that
the first character will be '2' because the \\( 3! \\) first permutations will
start with '0', the next \\( 3! \\) with '1'.

The 12th lexicographic permutations is obviously '2013'. It's just '0123', but
the '2' is place at the first position. Now that we have our first digit, we can
remove those 12 permutations from the 15th, which gives us 3 permutations.

Now, we are searching for the third lexicographic permutations of '013', with
the same reasoning, we can find that the first digit will be '1' after \\( 1 *
2! \\) permutations. It leaves use with 1 permutation and the string '03'.

After \\( 1 * 1! \\) permutations the first digit will be '3'. It leaves us with
'0' which is the last digit. The 15 lexicographic permutations is '2130' !

We just have to find the quotient and remainder of our nth permutations, the
divisor being the length of the string minus one. We can continue as long as our
string contains more than one character.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0024/solution2.py):

```python
def lexicographic_permutations(s, n):
    if len(s) <= 1:
        return s
    q, r = divmod(n, factorial(len(s) - 1))
    return s[q] + lexicographic_permutations(s[:q] + s[q + 1:], r)
```
