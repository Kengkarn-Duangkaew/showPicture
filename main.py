# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
def showPicture():
    pattern_input = int(input("Input Pattern: "))
    num_line = int(input("Please input line number: "))
    if (pattern_input == 1):
        pattern_a(num_line)
    elif (pattern_input == 2):
        pattern_b(num_line)
    elif (pattern_input == 3):
        pattern_c(num_line)


def pattern_a(num_line):
    for i in range(1, num_line):
        print("*" * i)


def pattern_b(num_line):
    for i in range(1, num_line):
        print("*" * i)
    for i in range(num_line, 0, -1):
        print("*" * i)


def pattern_c(num_line):
    count = 0
    count_2 = 0
    num_round = int(input("Input Round: "))
    delay = float(input("Input Dalay: "))
    num_di = int(input("Input Diamond: "))
    for j in range(num_round):
        count = 0
        count_2 = 0
        for i in range(num_line, 0, -1):
            time.sleep(delay)
            print(" " * i, end="")
            printDiamond(i, count, num_di, 1)
            count += 1
            if (i == num_line):
                print("*" * count, end="")
                print("")
            if (i <= num_line - 1):
                count_2 += 1
                print("*" * ((count_2 * 2) + 1))
        count = 0
        count_2 = num_line+1
        for i in range(num_line+1, 0, -1):
            time.sleep(delay)
            print(" " * count, end="")
            printDiamond(i, count, num_di, 2)
            count += 1
            if (i == num_line+1):
                print("*" * ((num_line * 2) + 1), end="")
                print("")
            if (i <= num_line):
                count_2 -= 1
                print("*" * ((count_2 * 2) - 1))

def printDiamond(i, count, num_di, checkUpDown):
    # 1=Up, 2=Down
    if (checkUpDown == 1):
        for j in range(num_di-1):
            print("*" * ((count * 2) + 1), end="")
            print(" " * (i * 2), end="")
    else:
        for j in range(num_di-1):
            print("*" * ((i * 2) - 1), end="")
            print(" " * ((count * 2)), end="")

showPicture()