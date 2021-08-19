# Prime factorization

The [Brute force](solution2.md) is actually very slow. A better solution can be
found using prime factorization. The key is to understand that when \\( x \\)
divides \\( y \\) evenly, it is because the prime factors of \\( x\\) are
contained in \\( y \\). For example, \\( 20 = 2^2 \* 5 \\) which means that a
number divisible by 20 is also divisible by 2, 4 and 5.

Calculating the prime factorization of each number from 1 to 20 give us:

\\[\begin{align} 20 &= 2^2 * 5\\\\ 19 &= 19\\\\ 18 &= 2 * 3^2\\\\ 17 &= 17\\\\ 16 &= 2^4\\\\ 15 &= 3 * 5\\\\ 14 &= 2 * 7\\\\ 13 &= 13\\\\ 12 &= 2^2 * 3\\\\ 11 &= 11\\\\ \end{align} \\]

We can stop here, because 10 is included in 20, 9 in 18, 8 in 16, 7 in 14, 6 in
12, 5 in 20, 4 in 20, 3 in 18, 2 in 20 and 1 in 20.

It gives us the answer: \\( 2^4 \* 3^2 \* 5 \* 7 \* 11 \* 13 \* 17 \* 19 =
232792560 \\).
