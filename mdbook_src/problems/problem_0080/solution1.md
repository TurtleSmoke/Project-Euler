# Square roots by subtraction

## Problem

We need to find the sum of the first one hundred decimal digits of the square roots of the first one hundred natural numbers.

## Understanding the problem

The problem is not difficult to understand, the challenge lies in determining the decimal digits of the square roots.

## Solution

We could use Python's decimal module, but that would not be very interesting.
Instead, we will use an algorithm that computes square roots digit by digit.
As usual, Wikipedia has [plenty to offer](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation).
I chose the [subtraction method](https://studylib.net/doc/7921494/square-roots-by-subtraction---jarvis--frazer) from Jarvis Frazer as it seemed the easiest to implement.

Let \\( a = 5n \\) and \\( b = 5 \\), where \\( n \\) is the number whose square root we want to compute.
We follow the following rules:

\\[
\begin{align}
    &(R1) \ If\ a\geqslant b,\ replace\ a\ with\ a-b,\ and\ add\ 10\ to\ b.\\\\
    &(R2) \ If\ a< b,\ add\ two\ zeroes\ to\ the\ end\ of\ a,\ and\ add\ a\ zero\ to\ b\ just\ before\ the\ final\ digit\.
\end{align}
\\]

The process is repeated until \\( b \\), which approximates the square root of \\( n \\), is greater than \\( 10^{p + 1} \\) where \\( p \\) is the precision.
In our case, \\( p = 100 \\).
The only special case is when \\( a = 0 \\), indicating that \\( n \\) is a perfect square, which si not considered in this problem.

The code is pretty straightforward:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0080/solution1.py):

```python
def square_root(n):
    a, b = 5 * n, 5
    while b < 10**101:
        if a >= b:
            a -= b
            b += 10
        else:
            # Perfect square
            if a == 0:
                return 0
            a *= 100
            b = (b // 10) * 100 + 5

    return b
```

To obtain the result, we just have to sum the digits of the first one hundred square roots:

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0080/solution1.py):

```python
def square_root_digital_expansion():
    return sum(int(c) for n in range(1, 101) for c in str(square_root(n))[:100])
```
