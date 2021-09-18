import datetime


def counting_sundays():
    res = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                res += 1

    return res


if __name__ == "__main__":
    print(counting_sundays())
