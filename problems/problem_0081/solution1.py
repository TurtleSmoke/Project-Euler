from read_file import read_file


def path_sum_two_ways(filename="matrix.txt"):
    matrix = read_file(filename)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[-1][-1]


if __name__ == "__main__":
    print(path_sum_two_ways())
