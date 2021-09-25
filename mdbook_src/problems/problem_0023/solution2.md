# Set

The [Brute Force](solution1.md) solution is extremely slow, the biggest issue is
how we determine if a number is the sum of two abundant numbers.

We are searching for any abundant numbers \\( a_1 \\) and \\( a_2 \\) such that
\\( a_1 + a_2 = n \\), which implies that \\(a_2 = n - a_2 \\). If \\( n - a_2
\\) is an abundant number, then \\( n \\) is the sum of two abundant numbers.

Finding a value in a list is slow because we need to go through the whole list,
that's why using a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type))
to store our abundant is more efficient in our this case. We just need to
iterate over all abundant once and check if \\( n \\) minus this abundant is
also in the set.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution2.py):

```python
any((i - a1 in abundants) for a1 in abundants)
```

We can also improve the way we build this set of abundant numbers. Since we have
an upper bound, we can construct the sum of divisors of all these numbers at
once. For every \\( i \\) and \\( j \\) such that \\( i \times j < limit \\),
the number \\( i \times j \\) has both \\( i \\) and \\( j \\) as divisors. We
just need to be aware that if \\( i = j \\) we need to add the divisor only
once.

We start with a list of 1 because 1 divides all numbers. Then we iterate with
\\( i \\) from 2 to \\( \left\lfloor\sqrt{limit}\right\rfloor \\) and \\( j \\)
from \\( i \+ 1 \\) (to avoid the case where \\( i = j \\)) to \\( i \times j >
limit \Leftrightarrow j > \left\lfloor \frac{limit}{i} \right\rfloor \\).

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution2.py):

```python
sum_of_factors = [1] * (n + 1)
for i in range(2, floor(sqrt(n)) + 1):
    sum_of_factors[i * i] += i
    for j in range(i + 1, (n // i) + 1):
        sum_of_factors[i * j] += i + j
```

In the previous solution, we first built the list of abundant numbers and then
searched for the number that was not a sum of two of them, since we always have
\\( a_1 <= a_2 \\) we can actually do both at the same time.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0023/solution2.py):

```python
def non_abundant_sums(n=28123):
    sum_of_factors = [1] * (n + 1)
    for i in range(2, floor(sqrt(n)) + 1):
        sum_of_factors[i * i] += i
        for j in range(i + 1, (n // i) + 1):
            sum_of_factors[i * j] += i + j

    abundants = set()
    res = 0

    for i in range(1, n + 1):
        if sum_of_factors[i] > i:
            abundants.add(i)
        if not any((i - a1 in abundants) for a1 in abundants):
            res += i

    return res
```
