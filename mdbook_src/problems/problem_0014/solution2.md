# Caching

The Collatz sequence of starting numbers \\( 4 \\) and \\( 8 \\) are actually
quite similar :
\\[
\begin{align} &Collatz(4) = 4 \rightarrow 2 \rightarrow 1\\\\ &Collatz(8) = 8 \rightarrow 4 \rightarrow 2 \rightarrow 1\\\\ \end{align} \\]

By calculating \\( Collatz(8) \\) we ended up recalculating \\( Collatz(4)
\\), if we keep in memory the number of iterations of \\( Collatz(4) \\), we
could reuse it to find the number of iterations of \\( Collatz(8) \\).

That is what [cache](https://en.wikipedia.org/wiki/Cache_(computing)) is,
storing data so that future requests for that data can be served faster.

In our case, when calculating the number of iteration of \\( n \\), we first
look if the value has already been computed, if not, we update the cache 
using the formula.

From [solution2.py](https://github.com/turtlesmoke/project-euler/blob/main/problems/problem_0014/solution2.py):

```python
def longest_collatz_sequence(n=1000000):
    cache = {1: 1}

    def collatz(i):
        if i not in cache:
            cache[i] = collatz(i // 2 if i % 2 == 0 else 3 * i + 1) + 1

        return cache[i]

    return max(range(1, n), key=collatz)
```
