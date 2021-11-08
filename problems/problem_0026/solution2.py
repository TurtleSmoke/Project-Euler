def find_cycle(n):
    while n % 2 == 0:
        n /= 2
    while n % 5 == 0:
        n /= 5

    if n == 1:
        return 0

    i = 1
    r = 10
    while r != 1:
        r = (r * 10) % n
        i += 1

    return i


def reciprocal_cycles(n=1000):
    max_cycle = 0
    res = 0
    for i in range(n, n // 2, -1):
        current_cycle = find_cycle(i)

        if current_cycle == i - 1:
            return i

        if current_cycle > max_cycle:
            max_cycle = current_cycle
            res = i

    return res


if __name__ == "__main__":
    print(reciprocal_cycles())
