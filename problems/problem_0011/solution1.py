from read_file import read_file


def largest_product_in_grid(filename):
    g = read_file(filename)

    for y in range(0, 20):
        for x in range(0, 17):
            yield g[x][y] * g[x + 1][y] * g[x + 2][y] * g[x + 3][y]
    for x in range(0, 20):
        for y in range(0, 17):
            yield g[x][y] * g[x][y + 1] * g[x][y + 2] * g[x][y + 3]
    for y in range(0, 17):
        for x in range(0, 17):
            yield g[x][y] * g[x + 1][y + 1] * g[x + 2][y + 2] * g[x + 3][y + 3]
    for x in range(3, 20):
        for y in range(0, 17):
            yield g[x][y] * g[x - 1][y + 1] * g[x - 2][y + 2] * g[x - 3][y + 3]


if __name__ == "__main__":
    print(max(largest_product_in_grid("given.txt")))
