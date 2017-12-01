#!/usr/bin/env python

import sys

def main1(input):

    sum = 0
    last_digit = input[-1]
    for digit in input:
        if(digit == last_digit):
            sum += int(digit)
        last_digit = digit

    print("output")
    print(sum)


def main2(input):

    length=len(input)
    sum = 0
    for index, digit in enumerate(input):
        if digit == input[index - int(length/2)]:
            sum += int(digit)

    print("output")
    print(sum)

if __name__ == "__main__":
    main2(sys.argv[1])
