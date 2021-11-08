# Carmichael function

The [Brute force](solution1.md) solution works and is not that slow. Yet, with a
few observations, we can improve it.

1. If you played a bit with the previous snippet of code, you might have notice
   that most of the duplicate digits are 1. That's not a coincidence, the first
   rest is also 1. In fact, what we are searching for is more known as the
   result of
   the [Carmichael function](https://en.wikipedia.org/wiki/Carmichael_function):

> The Carmichael function associates to every positive interger \\( n \\) a
> positive integer \lambda{n}, defined as the smallest positive integer \\(
> m \\) such that
> \\[ a^m \equiv 1\ \[ n \] \\]

In our case, \\( a \\) is always 10 and \\( m \\) is the length of the cycle we
are searching for the number \\( n \\).

Knowing that, we can try to make some observations:

2. Let \\( f=\frac{1}{2^{a} 5^{b}} \\), where \\( a,b\in\mathbb{Z}_{\geqslant 0}
   \\). f has a finite and non-recurring decimal
   representation. [Proof on Wikipedia](https://en.wikipedia.org/wiki/Decimal_representation#Finite_decimal_representations)
   .

3. If \\( \frac{1}{m} \\) is a repeating decimal and \\( \frac{1}{n} \\) is a
   terminating decimal, them \\( \frac{1}{mn} \\) has a nonperiodic part whose
   length is that of \\( \frac{1}{n} \\) and a repeating part whose length is
   that of \\( \frac {1}{m} \\).
   From [Wolfram MathWorld](https://mathworld.wolfram.com/RepeatingDecimal.html)

4. The recurring part of \\( \frac{1}{d} \\) cannot have more than \\( d - 1 \\)
   digits. [Proof on Wikipedia](https://en.wikipedia.org/wiki/Carmichael_function#Order_of_elements_modulo_n)

Let's try to use this information in our program:

We can reduce \\( n \\) by dividing it with \\( 2 \\) or \\( 5 \\) until it
become coprime with \\( 10 \\) (3). If after this reduction \\( n = 1 \\), \\(
\frac{1}{n} \\) has no recurring part (2).

We do not need to use a dictionary to find our cycle. Since \\( n \\) will be
coprime with 10, there will not be any leading number before the recurring
part (4). We know that if the rest is 1, we found our cycle (1).

```python
def find_cycle(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5

    if n == 1:
        return 0

    i = 1
    r = 10
    while r != 1:
        r = (r * 10) % n
        i += 1

    return i
```

We can start from 1000 and iterate until \\( \frac{n}{2} \\) (2). If we find \\(
n \\) such that \\( \lambda{n} == n - 1 \\), there will be no point to go any
further (4).

```python
def reciprocal_cycles(n=1000):
    max_cycle = 0
    res = 0
    for i in range(n, n // 2, -1):
        current_cycle = find_cycle(i)

        if current_cycle == i - 1:
            return i

        if current_cycle > max_cycle:
            max_cycle = current_cycle
            res = i

    return res
```