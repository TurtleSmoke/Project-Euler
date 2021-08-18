# Brute force

\\( i \\) is a factor of \\( n \\) if \\( n\ \equiv\ 0\ [i] \\), in our case it
is enough to iterate over each number. When a factor is found, we simply divide
\\( n \\) by that factor and continue as long as \\( n \\) is greater than one.
When \\( n \\) is equal to one, we simply return the current factor which is
also the largest.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0003/solution1.py):

```python
def largest_prime_factor(n=600851475143):
    res = 2
    while n != 1:
        if n % res == 0:
            n //= res
        else:
            res += 1
    return res
```
