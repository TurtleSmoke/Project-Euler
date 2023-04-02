def new_fraction(numerator, denominator):
    return denominator, 2 * denominator + numerator

def square_root_convergents():
    numerator = 0
    denominator = 1
    count = 0
    for _ in range(1000):
        numerator, denominator = new_fraction(numerator, denominator)
        if len(str(numerator + denominator)) > len(str(denominator)):
            count += 1
    return count


if __name__ == "__main__":
    print(square_root_convergents())
