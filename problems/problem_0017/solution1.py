def number_letter_counts():
    unit = len("onetwothreefourfivesixseveneightnine")
    ten = len("teneleventwelvethirfourfifsixseveneighnine") + len("ten") * 7
    and_l = len("and")
    twenty = len("twentythirtyfortyfiftysixtyseventyeightyninety")
    hun = len("hundred")
    thou = len("onethousand")
    return thou + 900 * hun + 190 * unit + 100 * twenty + 891 * and_l + 10 * ten


if __name__ == "__main__":
    print(number_letter_counts())
