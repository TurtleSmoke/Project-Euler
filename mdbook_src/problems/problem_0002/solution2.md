# Fibonacci recurrence

If we take a look at the Fibonacci series:

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...

Since our only concern is the parity of the numbers, with O being odd and E
even:

> E, O, O, E, O, O, E, O, O, E, O, O, E, O, O, E, ...

#### It seems that every third number of the series is even, let's try to prove it properly.

\\[ \begin{gather} If\ n=0\ then\ F_{0}=0\ is\ even\\\\\\\\ Assuming\ that\ F_ {3n} \ is\ even.\\\\ \\\\ F_{3( n+1)} =F_{3n+2} +F_{3n+1} =( F_{3n+1} +F_{3n}) +F_{3n+1} =2F_{3n+1} +F_ {3n}\\\\ \\\\ Since\ F_{3n} \ is\ even\ and\ 2F_{3n+1} \ is\ also\ even,\ we\ have\ F_{3( n+1)} \ even\\\\ because\ it\ is\ the\ sum\ of\ two\ even\ numbers. \end{gather} \\]

#### This mean that the series of even Fibonacci number is:

\\[ \begin {gather} E_{n} = F_{3n}\\\\ E_{n+2} = F_{3n+6} = F_{3n+5} + F_ {3n+4}\\\\ E_{n+2} = (F_{3n+4} + F_{3n+3}) + (F_{3n+3} + F_{3n+2})\\\\ E_{n+2} = (F_{3n+3} + F_{3n+2} + F_{3n+3}) + (F_{3n+3} + F_{3n+1} + F_{3n})\\\\ E_{n+2} = 3F_{3n+3} + (F_{3n+2} + F_{3n+1}) + F_{3n}\\\\ E_{n+2} = 4F_{3(n+1)} + F_{3n}\\\\ E_{n+2} = 4E_{n+1} + E_{n}\\\\ \end{gather} \\]

#### Which result int the following recurrence relation:

\\[ E_{n} = 4E_ {n-1} + E_{n-2} \\]

#### We are searching for:

\\[ \sum_{k=1}^ {n}E_k \\]

#### This can be simplified as follows:

\\[ \begin{align} \sum_{k=1}^{n}E_ {k+1} &= \sum_{k=1}^{n}4E_{k} + \sum_{k=1} ^{n}E_{k-1}\\\\ \sum_{k=1}^{n}E_{k}&= \frac{1}{4}(\sum_{k=1}^{n}E_{k+1} - \sum_{k=1}^{n}E_{k-1})\\\\ &= \frac{1}{4}(\sum_{k=2}^{n+1}E_{k} - \sum_{k=0}^{n-1}E_{k})\\\\ &= \frac{1}{4}(E_{n+1} + E_{n} - E_1 - E_0)\\\\ &= \frac{1}{4}(E_{n+1} + E_{n} - 2)\\\\ \end{align} \\]

The result can be calculated by iterating until \\( E_{n+1} \\) is greater than
the limit, so that \\( E_n \\) is less than the limit, then apply the previous
function.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0002/solution2.py):

```python
def sum_of_even_fibonacci_numbers(limit=4000000):
    e0 = 0
    e1 = 2
    while e1 < limit:
        e0, e1 = e1, 4 * e1 + e0

    return (e1 + e0 - 2) // 4
```
