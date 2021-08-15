def sum_of_three_and_five(limit=1000):
    sum_3 = sum(i for i in range(0, limit, 3) if i % 3 == 0)
    sum_5 = sum(i for i in range(0, limit, 5) if i % 5 == 0)
    sum_15 = sum(i for i in range(0, limit, 15) if i % 15 == 0)
    return sum_3 + sum_5 - sum_15


if __name__ == "__main__":
    print(sum_of_three_and_five())
