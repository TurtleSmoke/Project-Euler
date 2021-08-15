def sumOfThreeAndFive(limit):
    result = 0
    for i in range(0, limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

if __name__ == "__main__":
    print(sumOfThreeAndFive(1000))
