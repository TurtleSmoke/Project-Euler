def sum_of_three_and_five(limit=1000):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    print(sum_of_three_and_five())
