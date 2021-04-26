def spiralize(number):
    x = 1
    counter = 0
    incrt = 2
    total = 0

    while x <= number ** 2:
        total += x
        x += incrt
        counter += 1
        if counter == 4:
            incrt += 2
            counter = 0

    return total

if __name__ == "__main__":
    templ = """
def test_{0}():
    \"\"\" Test the {0} from the assignments. \"\"\"
    assert homework.spiralize({0}) == {1}
"""

    x = 11
    while x <= 501:
        answer = spiralize(x)
        print(templ.format(x, answer))
        x += 10