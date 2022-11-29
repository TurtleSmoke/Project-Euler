# Brute force

First, we need to know when the multiplicand/multiplier/product triplet is
pandigital. There are several ways to do this, probably the most obvious
being to convert the triplet to a single sorted string and compare it to
"123456789".

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0032/solution1.py):

```python
def is_pandigital(multiplicand, multiplier, product):
    return sorted(str(multiplicand) + str(multiplier) + str(product)) == list(
        "123456789")
```

One solution I really like uses a binary number to keep track of the digits.
This is faster than converting the triplet to a string and uses less memory
than a set or list. This method uses the bits as flags to check if a digit
is present. If one of the digits is used twice, the triplet is not
pandigital. If the final binary number is 0b1111111110, the triplet is
pandigital.

```python
def is_pandigital3(multiplicand, multiplier, product):
    digits = 0
    for n in (multiplicand, multiplier, product):
        while n:
            if digits & (1 << (n % 10)):
                return False
            digits |= 1 << (n % 10)
            n //= 10

    return digits == 0b1111111110
```

Next, we need to find all the possible multiplicand/multiplier/product
combinations. We can do this by brute force, trying all the possible
values for the multiplicand and multiplier from 1 to 987654321. But the
calculation will take too long.

We know that if the multiplier is 5 digits, then the result will be at least
5 digits, so the total number of digits will be at least 11 and therefore
not pandigital.

On the contrary, if the multiplier is 1 digit and the multiplicand 3 digits, the
result will be 4 digits and the total number of digits will be 8.

Trying different combinations of multiplicand and multiplier, we find that
only the following one result in a 9-digit triplet.

- 2 digits * 3 digits = product of 4 or 5 digits
- 1 digit * 4 digits = product of 4 or 5 digits

We can limit the search to these combinations. To avoid duplicates, we can
store the current pandigital products in a set and compute the sum at the end.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0032/solution1.py):

```python
def pandigital_products():
    products = set()
    for i in range(1, 100):
        for j in range(100 if i > 9 else 1000, 10000 // i + 1):
            if is_pandigital3(i, j, i * j):
                products.add(i * j)

    return sum(products)
```

