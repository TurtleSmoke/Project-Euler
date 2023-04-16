import itertools
from math import sqrt, floor


def get_convergent_cycle(n):
    a_0 = floor(sqrt(n))
    res = []
    if a_0 * a_0 == n:
        return []

    bn = a_0
    cn = 1

    for _ in itertools.count(1):
        cn = (n - (bn * bn)) / cn
        an = floor((sqrt(n) + bn) / cn)
        bn = -(bn - (an * cn))
        res.append(an)
        if an == 2 * a_0:
            return res


def diophantine_equation():
    x, res = 0, 0
    for d in range(2, 1001):
        an = get_convergent_cycle(d)
        if not an:
            continue

        h1, h2, k1, k2 = 1, floor(sqrt(d)), 0, 1
        for i in itertools.count(0):
            h1, h2 = h2, h1 + an[i % len(an)] * h2
            k1, k2 = k2, k1 + an[i % len(an)] * k2
            if h2 * h2 - d * k2 * k2 == 1:
                x, res = max((h2, d), (x, res))
                break

    return res


if __name__ == "__main__":
    print(diophantine_equation())
