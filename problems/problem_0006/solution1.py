def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))


def square_of_sum(n):
    return sum(i for i in range(1, n + 1))**2


def sum_square_difference(n=100):
    return square_of_sum(n) - sum_of_squares(n)


if __name__ == "__main__":
    print(sum_square_difference())
