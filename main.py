# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import termcolor
import os

def showPicture():
    os.system('color')
    pattern_input = int(input("Input Pattern: "))
    if (pattern_input == 1):
        pattern_a()
    elif (pattern_input == 2):
        pattern_b()
    elif (pattern_input == 3):
        pattern_c()
    elif (pattern_input == 4):
        pattern_d()


def pattern_a():
    num_line = int(input("Please input line number: "))
    for i in range(1, num_line):
        print("*" * i)


def pattern_b():
    num_line = int(input("Please input line number: "))
    for i in range(1, num_line):
        print("*" * i)
    for i in range(num_line, 0, -1):
        print("*" * i)


def pattern_c():
    num_line = int(input("Please input line number: "))
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
                print(termcolor.colored("*", 'red') * count, end="")
                print("")
            if (i <= num_line - 1):
                count_2 += 1
                print(termcolor.colored("*", 'red') * ((count_2 * 2) + 1))
        count = 0
        count_2 = num_line+1
        for i in range(num_line+1, 0, -1):
            time.sleep(delay)
            print(" " * count, end="")
            printDiamond(i, count, num_di, 2)
            count += 1
            if (i == num_line+1):
                print(termcolor.colored("*", 'red') * ((num_line * 2) + 1), end="")
                print("")
            if (i <= num_line):
                count_2 -= 1
                print(termcolor.colored("*", 'red') * ((count_2 * 2) - 1))

def printDiamond(i, count, num_di, checkUpDown):
    # 1=Up, 2=Down
    if (checkUpDown == 1):
        for j in range(num_di-1):
            if (j % 3 == 0):
                print(termcolor.colored("*", 'red') * ((count * 2) + 1), end="")
                print(" " * (i * 2), end="")
            elif (j % 3 == 1):
                print(termcolor.colored("*", 'green') * ((count * 2) + 1), end="")
                print(" " * (i * 2), end="")
            else:
                print(termcolor.colored("*", 'blue') * ((count * 2) + 1), end="")
                print(" " * (i * 2), end="")
    else:
        for j in range(num_di-1):
            if (j % 3 == 0):
                print(termcolor.colored("*", 'red') * ((i * 2) - 1), end="")
                print(" " * ((count * 2)), end="")
            elif (j % 3 == 1):
                print(termcolor.colored("*", 'green') * ((i * 2) - 1), end="")
                print(" " * ((count * 2)), end="")
            else:
                print(termcolor.colored("*", 'blue') * ((i * 2) - 1), end="")
                print(" " * ((count * 2)), end="")
def pattern_d():
    delay = float(input("Input Delay: "))
    num_space = 0
    count_round = 0
    max_conner = 30
    while (True):
        count_round += 1
        time.sleep(delay)
        if (count_round < 30):
            print(" " * num_space, end="")
            num_space += 1
            print(termcolor.colored("***", 'red'), end="")
            print(" " * ((max_conner * 2)), end="")
            max_conner -= 1
            print(termcolor.colored("***", 'blue'))
        if (count_round >= 30):
            print(" " * num_space, end="")
            num_space -= 1
            print(termcolor.colored("***", 'green'), end="")
            if (count_round == (30 * 2)):
                max_conner = 30
                count_round = 0
                num_space = 0
                print(" " * ((max_conner * 2)), end="")
            else:
                print(" " * ((max_conner * 2)), end="")
                max_conner += 1
            print(termcolor.colored("***", 'yellow'))

showPicture()