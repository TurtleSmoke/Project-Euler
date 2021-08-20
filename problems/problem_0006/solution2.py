def sum_square_difference(n=100):
    return (3 * n**4 + 2 * n**3 - 3 * n**2 - 2 * n) // 12


if __name__ == "__main__":
    print(1003**2)
    print(sum(2 * i + 1 for i in range(1003)))
    print(sum_square_difference())
