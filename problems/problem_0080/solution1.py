def square_root(n):
    a, b = 5 * n, 5
    while b < 10**101:
        if a >= b:
            a -= b
            b += 10
        else:
            # Perfect square
            if a == 0:
                return 0
            a *= 100
            b = (b // 10) * 100 + 5

    return b


def square_root_digital_expansion():
    return sum(int(c) for n in range(1, 101) for c in str(square_root(n))[:100])


if __name__ == "__main__":
    print(square_root_digital_expansion())
