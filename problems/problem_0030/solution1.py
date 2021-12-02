def digit_fifth_powers():
    return sum((n for n in range(2, 999999)
                if sum(int(i) ** 5 for i in str(n)) == n))


if __name__ == "__main__":
    print(digit_fifth_powers())
