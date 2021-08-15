def sum_of_three_and_five(limit=999):
    limit_3 = limit // 3
    limit_5 = limit // 5
    limit_15 = limit // 15

    sum_3 = 3 * (limit_3 * (limit_3 + 1) // 2)
    sum_5 = 5 * (limit_5 * (limit_5 + 1) // 2)
    sum_15 = 15 * (limit_15 * (limit_15 + 1) // 2)

    return sum_3 + sum_5 - sum_15


if __name__ == "__main__":
    print(sum_of_three_and_five())
