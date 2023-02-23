# Good old pen and paper

As is often the case with Project Euler problems, the problem can be solved with pen and paper.

Before anything, know that \\( [0-9] \\) means any digit between \\( 0 \\) and \\( 9 \\).

We know that the number to beat is \\( 918273645 \\), so any solution we find must be greater than that number.
We also know that the first multiplier is \\( 1 \\), so the first digit of our seed must start with \\( 9 \\).
We can discard any number in the form \\( 9[0-9], 9[0-9][0-9] \\) or any number greater than \\( 100000 \\), because none of them will result in a 9-digit number when multiplied by (1, 2, 3) or (1, 2, 3, 4).

Therefore, the solution must be of the form \\( 9[0-9][0-9][0-9] \\).

The solution must contain different digits and no zeros, because of the *1 multiplier.
It can not contain any 1 at all because it will be present twice.
One with the *1 multiplier and another because the *2 multiplier will result with the number of the form \\( 18[0-9][0-9] \\).

Therefore, the solution must be of the form \\( 9[2-9][2-9][2-9] \\).

We can continue these eliminations rules:

\\[
\begin{align}
&9[5-9][2-9][2-9] * 2 = 19[0-9][0-9][0-9] \text{, the *1 multiplier already contains a 9.}\\\\
&94[5-9][2-9] * 2 = 189[0-9][0-9] \text{, the *1 multiplier already contains a 9.}\\\\
&94[2-4][2-9] * 2 = 188[0-9][0-9] \text{, the double 8 is obviously wrong.}\\\\
&937[2-7] * 2 = 187[0-9][0-9] \text{, the *1 multiplier already contains a 7.}\\\\
&936[2-7] * 2 = 18724, 18726, 18728, 18730, 18732 \text{ or } 18734 \text{. They always lack the number 5 except for 18730 which have the number 4.}\\\\
&935[2-7] * 2 = 187[0-1][0-9] \text{, contains either a 0 or a double 1.}\\\\
&934[2-7] * 2 = 186[8-9][0-9] \text{, contains either a 9 or a double 8.}\\\\
&933[2-7]  \text{ is obviously wrong because of the double 3.}\\\\
&932[2-6] * 2 = 1864, 1866, 1868, 1870 \text{ or } 1872 \text{. They always lack the number 5 except for 1870 which lack the number 4.}\\\\
\end{align}
\\]

Thus, the number must be \\( 9327 \\). Indeed, \\( 9327 + 18654 \\) is the number we are looking for.
