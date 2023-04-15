def convergents_of_e():
    an = [2] + [1 if i % 3 != 2 else 2 * (i // 3 + 1) for i in range(1, 100)]
    h1, h2 = 0, 1
    for i in range(100):
        h1, h2 = h2, h1 + an[i] * h2
    return sum(int(c) for c in str(h2))


if __name__ == "__main__":
    print(convergents_of_e())
