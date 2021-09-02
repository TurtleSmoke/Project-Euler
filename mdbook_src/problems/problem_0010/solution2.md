# Summation minus summation

The sieve of eratosthenes is actually quite slow, it's possible to find a better
solution if we consider that we don't need to know all the primes to find their
sum. For example, the sum of the primes less than \\( 10 \\) is \\( 2 + 3 + 5 +
7 = 17 \\).

The sum of the primes less than \\( 10 \\) is the sum of the numbers less than
10 minus the sum of the multiples of the primes less than \\( \sqrt{10} \\)
plus the primes themselves minus \\( 1 \\). In this example, the sum of the
multiples of \\( 2 \\) and \\( 3 \\):

\\[ \begin{align} P &= 1+2+3+4+5+6+7+8+9+10\\\\ &- (\ +2\ \ \ \ \ \ \ +4\ \ \ \ \ \ \ +6\ \ \ \ \ \ +8\ \ \ \ \ \ \ +10)\\\\ &- (\ \ \ \ \ \ \ +3\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ +6\ \ \ \ \ \ \ \ \ \ \ \ \ +9) \ \ \ \ \ \ \ \ \ +6\\\\ &+ 2 + 3 - 1\\\\ \end{align} \\]

There is just one problem, the number \\( 6 \\) is both a multiple of \\( 2 \\)
and \\( 3 \\). This means we have to remove the multiple of \\( 3 \\) but not
the multiple of \\( 6 \\). For numbers larger than 10, if we continue with \\( 5
\\) we have to remove the multiple of \\( 5 \\) but not the multiple of \\(
2\*5=10 \\), \\( 3\*5=15 \\) and \\( 5*6=30 \\).

Let \\( \phi(n) \\) be the sum of the numbers less than \\( n \\).

We have the following sequence:

\\[ \begin{align} T_0(n) &= \phi(\left\lfloor n \right\rfloor) &&= 1+2+3+\dots\\\\ T_1(n) &= 2\left(T_0\left(\frac{n}{2}\right)\right) = 2\phi\left (\left\lfloor \frac{n} {2} \right\rfloor \right) &&= 2+4+6+\dots\\\\ T_2(n) &= 3\left(T_0\left(\frac{n}{3}\right) - T_1\left(\frac{n}{3}\right) \right) = 3\phi \left(\left\lfloor \frac{n}{3} \right\rfloor\right) - 6\phi\left(\left\lfloor \frac{n}{6} \right\rfloor\right) &&= 3+9+15+\dots\\\\ T_3(n) &= 5\left(T_0\left(\frac{n}{5}\right) - T_1\left(\frac{n}{5}\right) - T_2\left(\frac{n}{5}\right) \right) = 5\phi\left(\left\lfloor\frac{n}{5}\right\rfloor\right) - 10\phi\left(\left\lfloor\frac{n}{10}\right\rfloor\right) - 15\phi\left(\left\lfloor\frac{n}{15} \right\rfloor\right) + 30\phi\left(\left\lfloor\frac{n}{30} \right\rfloor\right) &&= 5+25+35+\dots\\\\ \end{align} \\]

So the k-th term is:

\\[ T_k(n) = p_k\left(T_0\left(\frac{n}{p_k}\right) - \dots - T_{k-1}\left (\frac{n} {p_k}\right)\right) \\]

Where \\( p_k \\) is the k-th prime.

We can create a function to find \\( T_k \\) if we have \\( p_k \\):

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0010/solution2.py):

```python
def tk(n, k):
    pk = primes[k - 1]
    t0 = phi(floor(n / pk))
    tn = sum([tk(n / pk, i) for i in range(1, k)])
    return pk * (t0 - tn)
```

The sum of the primes less than \\( n \\) is the sum of the numbers less than
\\( n \\) minus the sum of all the multiples of the primes less than \\( \sqrt
{n} \\) plus the primes themselves minus \\( 1 \\):

\\[ \left(T_0(n) - T_1(n) - \dots - T_k(n)\right) + \left(p_1 + p_2 + \dots + p_k\right) - 1 \\]

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0010/solution2.py):

```python
def summation_of_primes(limit=2000000):
    phi = lambda x: x * (x + 1) // 2
    primes = list(sieve.primerange(floor(sqrt(limit)) + 1))

    def tk(n, k):
        pk = primes[k - 1]
        t0 = phi(floor(n / pk))
        tn = sum([tk(n / pk, i) for i in range(1, k)])
        return pk * (t0 - tn)

    return phi(limit) - sum([tk(limit, i + 1) for i in range(len(primes))]) \
           + sum(primes) - 1
```
