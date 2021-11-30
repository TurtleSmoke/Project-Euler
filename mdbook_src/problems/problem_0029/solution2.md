# Discarding duplicate

We can actually solve this problem with pen and paper.

I won't explain the solution since `jorgbrown` has already done a great job in
his [post](https://projecteuler.net/thread=29;page=3#6162):
> Suppose \\( a \\) is a perfect square of the smaller \\( a \\), but not a
> square of a square. Then we have a duplicate when \\( b \\) is \\( 2, 3,
> 4\dots \\) up to \\( 50 \\). That is, \\( 49 \\) duplicates.
>
> Suppose \\( a \\) is a perfect cube of a smaller \\( a \\). When \\( b \\)
> is \\( 2 \\) through \\( 33 \\), we have duplicates of smaller \\( a \\)
> raised to the power \\( b\times3 \\). When \\( b \\) is \\( 34, 36, 38, 40,
> 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66 \\), we have duplicates
> of a smaller \\( a \\) raised to the power \\( (\frac{b}{2})\times3 \\).
> Total is \\( 32 + 17 \\), or again, \\( 49 \\) duplicates.
>
> Suppose \\( a \\) is the square of the square of a smaller \\( a \\). When
> \\( b \\) is \\( 2 \\) through \\( 49 \\), we have duplicates of the square
> root of a raised to the power \\( (b\times2) \\).  
> When \\( b \\) is \\( 51, 54, 57, 60, 63, 66, 69, 72, \\) or \\( 75, \\) we
> have dupes of \\( a^{(\frac{3}{4})} \\) raised to the power \\( \frac
> {b\times4} {3} \\). Total is \\( 49 + 9 \\), or \\( 58 \\).
>
> Suppose \\( a \\) is the fifth power of a smaller \\( a \\). We have dupes of
> fifth root of a raised to the power \\( (b\times5) \\), which covers \\( b \\)
> from \\( 2 \\) to \\( 20 \\). Then we have dupes of \\( a^{(\frac{2}{5})} \\)
> raised to the power \\( \frac{b\times5}{2} \\), which covers \\( b \\) of
> \\( 22, 24, 26, 28, 30, 32, 34, 36, 38, 40 \\). Then we have dupes of \\(
> a^{(\frac{3}{5})} \\) raised to the power \\( \frac{b\times5}{3} \\), which
> covers \\( b \\) of \\( 21, 27, 33, 39, 42, 45, 48, 51, 54, 57, 60 \\).
> Last, we have dupes of \\( a^\frac{4}{5} \\) raised to the power \\(
> \frac{b\times5}{4} \\), which covers \\( b \\) of \\( 44, 52, 56, 64, 68, 72,
> 76\\), and \\( 80 \\). Total dupes: \\( 48 \\).
>
> And the last power we have to worry about is \\( 6 \\). We have dupes of the
> square root of a raised to power \\( (b\times2) \\), which covers \\( b \\)
> from \\( 2 \\) to \\( 50 \\). Then we have dupes of the sixth root to the power
> \\( \frac{b\times6}{4} \\), which covers \\( b \\) of \\( 52 \\),
> \\( 54, 56, 58, 60, 62, 64, 66 \\). And last we have dupes of the sixth
> root to the power \\( \frac{b\times6}{5} \\), which covers \\( b \\) of \\(
> 55,
> 65, 70, 75 \\), and \\( 80 \\). Total dupes: \\( 62 \\).
>
> Now let's put it all together:
>
> squares: \\( 4, 9, 25, 36, 49, 100 \\): These \\( 6 \\) squares have \\(
> 49 \\) dupes each, \\( 6 \times 49 \\) = \\( 294 \\)
>
> cubes: \\( 8, 27 \\): These \\( 3 \\) cubes have \\( 49 \\) duplicates
> each: \\( 2 \times 49 = 98 \\)
>
> 4th power: \\( 16, 81 \\). These \\( 2 \\) have \\( 58 \\) dupes each: \\( 2
> \times 58 = 116 \\)
>
> 5th power: \\( 32 \\). This has \\( 48 \\) dupes.
>
> 6th power: \\( 64 \\): this has \\( 62 \\) dupes.
>
> Total # dupes: \\( 618 \\). \\( 9801-618 \\) is \\( 9183 \\).
> 