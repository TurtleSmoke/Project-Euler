def digit_factorial_chains():
    res = 0
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    for i in range(1, 1000000):
        found = set()
        while i not in found:
            found.add(i)
            i = sum([factorials[int(digit)] for digit in str(i)])
        if len(found) == 60:
            res += 1
    return res


if __name__ == "__main__":
    print(digit_factorial_chains())
