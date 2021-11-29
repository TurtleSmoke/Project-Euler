def number_spiral_diagonals(n=1001):
    m = (n - 1) // 2
    return int(1 + (16 / 3) * m ** 3 + 10 * m ** 2 + (26 / 3) * m)


if __name__ == "__main__":
    print(number_spiral_diagonals())
