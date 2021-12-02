def build_combination(d, n=0, s=''):
    if d == 0:
        yield s
    else:
        for i in range(n, 10):
            for v in build_combination(d - 1, i, s + str(i)):
                yield v


def digit_fifth_powers():
    cache = [i ** 5 for i in range(0, 10)]
    res = 0
    for n in build_combination(6):
        total = sum(cache[int(c)] for c in n)
        if sum(cache[int(c)] for c in str(total)) == total:
            res += total

    return res - 1


if __name__ == "__main__":
    print(digit_fifth_powers())
