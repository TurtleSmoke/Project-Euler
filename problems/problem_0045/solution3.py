def triangular_pentagonal_and_hexagonal():
    x_n = lambda x_i, y_i: 97 * x_i + 112 * y_i - 44
    y_n = lambda x_i, y_i: 84 * x_i + 97 * y_i - 38

    x, y = 1, 1
    x, y = x_n(x, y), y_n(x, y)
    y = y_n(x, y)
    return y * (2 * y - 1)


if __name__ == "__main__":
    print(triangular_pentagonal_and_hexagonal())
