# With pen and paper

In [Factorisation is the key](solution2.md), we assume that the number was of
the form \\( abccba \\). Since it is the factor of two 3-digit number, we have :

\\[ \begin{align} abccba &= (100a + 10b + c)(100d + 10e + f)\\\\ &= 10000ad + 1000(bd + ae) + 100(cd + be + af) + 10(ce + bf) + cf \end{align} \\]

Assuming the first digit is 9, then \\( cf \\) must be equal to 9 as well.

The only ways to make the last digit nine are:

\\[ 1 * 9\\\\ 3 * 3\\\\ 7 * 7 \\]

Thus, both number must start with 9 and end with either 1, 3, 7 or 9. We also
know that \\( 100a + 10b + c \\) or \\( 100d + 10e + f \\) is divisible by 11.
The only numbers divisible by 11 and ending with 1, 3, 7 or 9 in the
\\( [900; 999]
\\) are :

\\[ 913\\\\ 957\\\\ 979 \\]

This give us:

\\[ \text{a = 9}\\\\ \text{b = 1, 5 or 7}\\\\ \text{c = 3, 7 or 9}\\\\ \\]

Resulting in the numbers:

\\[
(900 + 10 + 3)(900 + 10e + 3) = 824439 + 9130x\\\\
(900 + 50 + 7)(900 + 10e + 7) = 867999 + 9570x\\\\
(900 + 70 + 9)(900 + 10e + 1) = 882079 + 9790x \\]

The first number implies that \\( e \\) is equal to 9 because if \\( e \\) was 
equal to 8, then \\(824439 \* 9130 \* 8 = 897479 \\) would not start with 9. 
With \\( e = 9 \\) we have \\( 913 \* 993 \\) which is the correct answer. 
Both \\( (900 + 50 + 7)(900 + 10e + 7) \\) and \\( (900 + 70 + 9)(900 + 
10e + 1) \\) give smaller palindrome.
