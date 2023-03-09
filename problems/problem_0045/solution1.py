def tn(n):
    return n * (n + 1) // 2


def pn(n):
    return n * (3 * n - 1) // 2


def hn(n):
    return n * (2 * n - 1)


def triangular_pentagonal_and_hexagonal():
    t, p, h = 286, 166, 144
    ti, pi, hi = tn(t), pn(p), hn(h)
    while not ti == pi == hi:
        if ti < pi:
            t += 1
            ti = tn(t)
        elif pi < hi:
            p += 1
            pi = pn(p)
        else:
            h += 1
            hi = hn(h)
    return ti


if __name__ == "__main__":
    print(triangular_pentagonal_and_hexagonal())
