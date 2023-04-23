# Euler's totient function

The [Euler's totient function](https://en.wikipedia.org/wiki/Euler%27s_totient_function) is defined as \\( \phi(n) \\).
There are several formulae for computing \\( \phi(n) \\), one of which is the following:

\\[ \phi(n) = n \prod_{p \in \mathcal{P}} \left( 1 - \frac{1}{p} \right) \\]

where \\( \mathcal{P} \\) is the set of prime factors of \\( n \\).

Remembering that the solution is \\( n \\) for which \\( \frac{n}{\phi(n)} \\) is a maximum, which is equivalent to finding \\( n \\) for which \\( \frac{\phi(n)}{n} \\) is a minimum, we can rewrite the above formula as

\\[ \frac{\phi(n)}{n} = \prod_{p \in \mathcal{P}} \left( 1 - \frac{1}{p} \right) \\]

Obviously, this is minimized when \\( \mathcal{P} \\) is large, therefore the solution is the number which has the largest number of prime factors.

In our case, \\( n \leq 1000000 \\), so the solution is \\( 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 = 510510 \\).
