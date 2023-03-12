from functools import reduce


def mod_pow(b, e, mod):
    return reduce(lambda acc, _: (acc * b) % mod, range(e), 1)


def self_powers():
    mod = 10**10
    sums = (mod_pow(i, i, mod) for i in range(1, 1001))
    return reduce(lambda acc, y: (acc + y) % mod, sums)


if __name__ == "__main__":
    print(self_powers())
