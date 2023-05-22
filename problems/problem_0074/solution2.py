def digit_factorial_chains():
    res = 0
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    cache = {}
    for i in range(1, 1000000):
        found = []
        while i not in found and i not in cache:
            found.append(i)
            i = sum([factorials[int(digit)] for digit in str(i)])
        for j, v in enumerate(found):
            cache[v] = len(found) - j + cache.get(i, 0)
            if cache[v] == 60:
                res += 1
    return res


if __name__ == "__main__":
    print(digit_factorial_chains())
