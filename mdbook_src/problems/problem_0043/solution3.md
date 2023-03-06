# With pen and paper

As often with these problems, it is possible to find the solution by hand.
The crucial aspect of these solutions is reducing the set of potential solutions.

The \\( d_4d_5d_6 \\) must be divisible by \\( 5 \\), thus \\( d_6 \\) must be \\( 0 \\) or \\( 5 \\).
If \\( d_6 = 0 \\), \\( 0d_7d_8 \\) must be divisible by \\( 11 \\), which implies that \\( d_7 = d_8 \\).
This is a contradiction since the number is pandigital, thus \\( d_6 \\) must be \\( 5 \\).

All the number \\( 5d_7d_8 \\) that can be divided by \\( 17 \\) are: \\( 506, 517, 528, 539, 550, 561, 572, 583 \\) and \\( 594 \\), but \\( 550 \\) is not pandigital.
Let us now check the number \\( d_6d_7d_8 \\) that are divisible by \\( 13 \\), with \\( d_6d_7 \\) being defined with the above solution:

- \\( 06x \Rightarrow x = 5 \\), but \\( 5 \\) is already used.
- \\( 17x \\) has no solution.
- \\( 28x \Rightarrow x = 6\\), gives \\( 286 \\) as a possible solution.
- \\( 39x \Rightarrow x = 0 \\), gives \\( 390 \\) as a possible solution.
- \\( 61x \Rightarrow x = 1 \\), but \\( 1 \\) is already used.
- \\( 72x \Rightarrow x = 8 \\), gives \\( 728 \\) as a possible solution.
- \\( 83x \Rightarrow x = 2 \\), gives \\( 832 \\) as a possible solution.
- \\( 94x \Rightarrow x = 9 \\), but \\( 9 \\) is already used.

The current only possible solution for \\( d_6d_7d_8d_9 \\) are \\( 5286, 5390, 5728\text{ and }5832 \\).

We can continue with the same process for the divisibility by \\( 17 \\):

- \\( 86x \Rightarrow x = 7 \\), gives \\( 867 \\) as a possible solution.
- \\( 90x \Rightarrow x = 1 \\), gives \\( 901 \\) as a possible solution.
- \\( 28x \Rightarrow x = 9 \\), gives \\( 289 \\) as a possible solution.
- \\( 32x \Rightarrow x = 3 \\), but \\( 3 \\) is already used.

The current only possible solution for \\( d_6d_7d_8d_9d_{10} \\) are \\( 52867, 53901\text{ and }57289 \\).

We can continue with the same process for the divisibility by \\( 7 \\):

- \\( x52 \Rightarrow x = 2 \\) or \\( x = 9 \\), but \\( 2 \\) is already used, gives \\( 952 \\) as a possible solution.
- \\( x53 \Rightarrow x = 5 \\), but \\( 5 \\) is already used.
- \\( x57 \Rightarrow x = 3 \\), gives \\( 357 \\) as a possible solution.

The current only possible solution for \\( d_5d_6d_7d_8d_9d_{10} \\) are \\( 952867, \text{ and }357289 \\).

For \\( d_2d_3d_4 \\) to be divisible by \\( 2 \\), \\( d_4 \\) must be even, with the remaining possible digits being \\( 0 \\) or \\( 4 \\) for \\( 952867 \\) and \\( 0, 4 \\) or \\( 6 \\) for \\( 357289 \\).

Thus, the only possible solutions are for \\( d_4d_5d_6d_7d_8d_9d_{10} \\) are \\( 0952867\\), \\( 4952867 \\), \\( 0357289 \\), \\( 4357289 \\), and \\( 6357289 \\).

The last divisibility property requires \\( d_3d_4d_5 \\) to be divisible by \\( 3 \\), which implies that \\( d_3 + d_4 + d_5 \\) must be divisible by \\( 3 \\).
With the remaining digits, we can check all the possible solutions:

- \\( x09 \Rightarrow x = 3 \\), gives \\( 309 \\) as a possible solution.
- \\( x49 \\) has no solution with the available digit \\( 0 \\), \\( 1 \\), or \\( 3 \\).
- \\( x03 \Rightarrow x = 6 \\), gives \\( 603 \\) as a possible solution.
- \\( x43 \\) has no solution with the available digit \\( 0 \\), \\( 1 \\), or \\( 6 \\).
- \\( x63 \Rightarrow x = 0 \\), gives \\( 063 \\) as a possible solution. 

The current only possible solution for \\( d_3d_4d_5d_6d_7d_8d_9d_{10} \\) are \\( 30952867 \\), \\( 60357289 \\), and \\( 06357289 \\).
All permutations of these numbers with the remaining digits give a solution that satisfies the divisibility property.

The sum of all this numbers is the solution to the problem.
