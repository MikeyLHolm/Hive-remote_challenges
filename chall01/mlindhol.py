#!/usr/bin/env python3
import sys


def error():
    print("usage: ./" + sys.argv[0] + "<a-zA-Z string>")
    exit(-1)


def main():

    if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
        error()

    morse_array = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                   "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    input_str = sys.argv[1]

    for x in input_str:
        av = ord(x)
        if av < 32 or 32 < av < 65 or 90 < av < 97 or av > 122:
            error()

    for s in input_str:
        if s is " ":
            print(" ", end="")
        else:
            y = 64 if s.isupper() else 96
            letter = ord(s) - y
            print(morse_array[letter - 1], end="")


if __name__ == "__main__":
    main()
