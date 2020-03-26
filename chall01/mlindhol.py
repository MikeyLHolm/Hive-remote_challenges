#!/usr/bin/env python
import sys


def error():
    print("usage: ./mlindhol.py <a-zA-Z string>")
    exit(-1)


if len(sys.argv) != 2 or len(sys.argv[1]) == 0:
    error()

morse_array = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
               "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

input_str = sys.argv[1]

if any(x.isalpha() is False and x.isspace() is False for x in input_str):
    error()

i = 0;
while i < len(input_str):
    if input_str[i] is " ":
        print(" ", end="")
        i += 1
    else:
        y = 64 if input_str[i].isupper() else 96
        letter = ord(input_str[i]) - y
        print(morse_array[letter - 1], end="")
        i += 1
