# Combination

For a square of dimension \\( n \\), we know that whatever path we take, there
will be exactly \\( n \\) movements to the right and \\( n \\) movements down.
We can represent the path as a string of 'D' for down and 'R' for right.

For example, with a \\( 3 \times 3 \\) square, a path could be : 'RRRDDD',
'DDDRRR' or 'RDDRDR'. The question now is, 'In how many ways can we place the '
R' and the 'D' in the string ?'

Since there must be as many 'D' as 'R', we can only place the 'R' and leave the
rest as 'D'. That means we are searching for the number of ways we can place \\(
n \\) 'R' in a string of \\( 2n \\) characters. This is called
a [combination](https://en.wikipedia.org/wiki/Combination), in our case, it's:

\\[ \begin{pmatrix} 2n\\\\ n \end{pmatrix} = \frac{\left(2n\right)!}{n!\left(2n - n\right)!} = \frac{\left (2n\right)!}{\left(n!\right)^2} \\]

This can be calculated using factorial:

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0015/solution3.py):

```python
def lattice_paths(n=20):
    return factorial(2 * n) // (factorial(n) ** 2)
```
