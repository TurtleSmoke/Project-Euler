# Prime number theorem

As I said in the [Brute force](solution1.md) solution, the fasted way to
generate primes is the sieve of eratosthenes, but it requires an upper bound. We
can not find the exact upper bound, but we can have a good approximation using
the [Prime number theorem](https://en.wikipedia.org/wiki/Prime_number_theorem):

\\[  \pi(N) \sim \frac{N}{\log(N)} \\]

Where \\( \pi(N) \\) is the
[prime-counting function](https://en.wikipedia.org/wiki/Prime-counting_function)
.

This function give the number of primes \\( M \\) less than or equal to \\( N
\\), in our case we want to determine \\( N \\) knowing \\( M \\). Which give us
another formula:

\\[ \begin{align} \frac{N}{\log(N)} &\leqslant M\\\\ \frac{\log(N)}{N} &\leqslant \frac{1}{M}\\\\ -\frac{\log(N)}{N} &\leqslant -\frac{1}{M}\\\\ -\frac{\log(N)}{e^{\log(N)}} &\leqslant -\frac{1}{M}\\\\ -\log(N)e^{-\log(N)} &\leqslant -\frac{1}{M} \end{align} \\]

The [Lambert \\( W \\) function](https://en.wikipedia.org/wiki/Lambert_W_function)
says that \\( we^w = z \Leftrightarrow w = \mathit{W}_{k}(z) \\). This give us:

\\[ \begin{align} -\log( N) e^{-\log( N)} &\leqslant -\frac{1}{M}\\\\ -\log( N) &\leqslant W_{k}\left( -\frac{1}{M}\right)\\\\ N &\leqslant e^{-W_{k}\left( -\frac{1}{M}\right)} \end{align} \\]

The solutions of Lambert's \\( W \\) function with real number can be found with
ony two branches: \\( W_0 \\) and \\( W_{-1} \\) suffice.

For real number \\( z \\) and \\( w \\) the equation \\( we^w = z \\) can be
solved for \\( w \\) only if \\( w \geqslant -\frac{1}{e} \\). if \\( z
\geqslant 0 \\) we get \\( w = W_0(z) \\) and the two values \\( w = W_0(z) \\)
and \\( w = W_{-1}(z) \\) if \\( -\frac{1}{e} \leqslant w < 0 \\).

We have \\( w = -\log(N) \\) so we are in the second case. We need to determine
which of \\(W_0(z) \\) and \\( W_{-1}(z) \\) is the right formula.

The branch 0 converge to 1 when \\( z \\) converge to 0. Actually, for \\( M >
3 \\) we have \\( \lceil W_k(-\frac{1}{M}) \rceil = 1\\). It implies that the
good branch is -1.

We can actually build the sieve of eratosthenes with the upper bound \\( e^ {-W_
{-1}(-\frac{1}{M})} \\). Lambert's \\( W \\) function cannot be expressed in
terms of
[elementary functions](https://en.wikipedia.org/wiki/Elementary_function), so
the formula cannot be simplified. The value of Lambert's \\( W \\) function
requires an iterative method to be found, as this is quite a difficult problem
we will use the
[lambertw](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.lambertw.html)
from [scipy](https://docs.scipy.org/doc/scipy/index.html) to determine our upper
bound.

From [solution3.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0007/solution3.py):

```python
def n_th_prime(n=10001):
    if n < 3:
        return [2, 3][n - 1]

    limit_pi_1 = ceil(exp(-lambertw(-1 / n, -1).real))
    primes = sieve.primerange(limit_pi_1 + 1)

    return next(islice(primes, n - 1, n))
```

Note that `sieve.primerange` returns a `generator`, so we use slice to get the
n-th element.

When \\( N < 3 \\), we have \\( -\log(N) \geqslant -\frac{1}{e} \\) which means
the Lambert's W function has no solution. We can simply hard-code the case of 1
and 2.
