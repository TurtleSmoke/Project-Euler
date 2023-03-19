# Cumulative sum

The [Brute force](./solution1.md) approach has a time complexity of \\( O(n^3) \\), due to the double loop and the computation of the sum of consecutive primes at each iteration.
However, the Sieve of Eratosthenes used for generated the primes has a time complexity of \\( O(n\log(\log(n))) \\), suggesting that it might be possible to improve the brute force approach.

A major drawback of the brute force approach is the computation of the sum of consecutive primes at each iteration.
This can be optimized by using a cumulative sum, which has the additional benefit that the sum of consecutive primes between \\( i \\) and \\( j \\) is equal to \\( S_j - S_i \\), where \\( S_i \\) is the cumulative sum of the first \\( i \\) primes.
Therefore, searching for the sum of any consecutive primes can be done in constant time.

To effectively iterate over all possible combinations of consecutive primes, it's best to start from the longest possible sequence and then decrease the size of the sequence until a sum is prime.
This sequence can be obtained by finding the first cumulative sum that is greater than \\( 1000000 \\) since it is obvious that the sequence must start from the first prime.
Using a binary search this window size can be found in \\( O(\log(n)) \\).

The remaining step involve iterating over all the possible windows of consecutive primes until a sum is prime.
Using a set to store the primes can further improve the time complexity of searching if a sum is prime.

In theory, the time complexity of this approach is \\( O(wn) \\), where \\( w \\) is the size of the longest window and \\( n \\) is the number of primes below \\( 1000000 \\).
Estimating \\( w \\) based on the size of \\( n \\) is difficult, but it's clear that it is much smaller than \\( n \\).
For example in our case \\( w \\) is \\( 546 \\) and \\( n \\) is \\( 664579 \\).
In practice, this approach only take a couple of iterations since \\( w \\) is very small, and the iteration is done starting from the largest window.

From [solution2.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0050/solution2.py):

```python
def consecutive_prime_sum(lim=10**6):
    primes = list(sieve.primerange(2, lim))
    primes_set = set(primes)
    cumul_sum = list(accumulate(primes))
    max_window = bisect.bisect_left(cumul_sum, lim)
    for window in range(max_window, 0, -1):
        for i in range(len(cumul_sum) - window):
            s = cumul_sum[i + window] - cumul_sum[i]
            if s >= lim:
                break
            if s in primes_set:
                return s
```
