from read_file import read_file


def maximum_path_sum_I(filename):
    triangle = read_file(filename)

    def path(i, j):
        if i >= len(triangle) or j >= len(triangle[i]):
            return 0

        return triangle[i][j] + max(path(i + 1, j), path(i + 1, j + 1))

    return path(0, 0)


if __name__ == "__main__":
    print(maximum_path_sum_I("given.txt"))
