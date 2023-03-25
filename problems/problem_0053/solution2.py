def combinatoric_selections():
    res = 0
    for n in range(23, 101):
        ncr = n
        for r in range(2, n // 2 + 1):
            ncr = (ncr * (n - r + 1)) // r  # Observation 2
            if ncr > 1000000:
                res += n - 2 * r + 1  # Observation 1
                break
    return res


if __name__ == "__main__":
    print(combinatoric_selections())
