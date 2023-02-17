# Brute force

First of all, we need to understand how the lexicographic permutations are
computed. If we enumerate all the permutations of '0123' starting with '0':

\\[ 0123\\\\ 0132\\\\ 0213\\\\ 0231\\\\ 0312\\\\ 0321\\\\ \\]

By removing the '0' we get:

\\[ 123\\\\ 132\\\\ 213\\\\ 231\\\\ 312\\\\ 321\\\\ \\]

It's the lexicographic permutations of '123' !

We can continue:

\\[\begin{align} &123\ &&213\ &&321\\\\ &132\ &&231\ &&321 \end{align} \\]

By removing the first character each time, it gives:

\\[\begin{align} &23\ &&13\ &&21\\\\ &32\ &&31\ &&21 \end{align} \\]

That is, the lexicographic permutations of '23', '13', and '21',

Now, enumerating all permutations of '0123' starting with '1':

\\[ 1023\\\\ 1032\\\\ 1203\\\\ 1230\\\\ 1302\\\\ 1230 \\]

By removing the '1' we get:

\\[ 023\\\\ 032\\\\ 203\\\\ 230\\\\ 302\\\\ 230 \\]

It's the lexicographic permutations of '023' !

This means that we can compute all the lexicographic permutations of a string by
taking each character, placing it at the beginning of the new permutations and
then adding the lexicographic permutations of the rest of the string
recursively.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0024/solution1.py):

```python
def lexicographic_permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for p in lexicographic_permutations(s[:i] + s[i + 1 :]):
                yield s[i] + p
```

By using `yield`, we create a generator, it's better than storing 1 million
elements and then returning the last one, just take the 1000000th element
generated.
