from read_file import read_file


def maximum_path_sum_II(filename):
    triangle = read_file(filename)

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


if __name__ == "__main__":
    print(maximum_path_sum_II("triangle.txt"))
