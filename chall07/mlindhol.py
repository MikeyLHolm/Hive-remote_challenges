#!/usr/bin/env python
# python 3.8.2 Windows 10

import sys

# sys.exit("usage: ./" + sys.argv[0] " <1-9 squared_rows...>")
def validate(lines, n):
    for i in lines:
        if len(i) != n:
            sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

def top(min, max, lines):
    while min <= max:
        print(lines[min] + ", ")
        min += 1

def right(min, max, lines):
    while min < max:
        print(lines[min][max] + ", ")
        min += 1

def bottom(min, max, lines):
    while min <= max:
        print(lines[max] + ", ")
        max -= 1

def left(min, max, lines):
    while min < max:
        print(lines[min - 1][max] + ", ")
        max -= 1

def solve(lines, n):
    min = 0
    max = n - 1
    ret = []

    while min <= max:
        print("hello again")
        top(min, max, lines[min])
        min += 1
        right(min, max, lines)
        bottom(min, max, lines[max])
        max -= 1
        left(min, max, lines)

    print(ret)

def main():
    if len(sys.argv) == 1:
        sys.exit("usage: " + sys.argv[0] + " <1-9 squared_rows...>")

    lines = sys.argv[1:]
    n = len(lines)

    validate(lines, n)
    print(lines)
    print(n)

    solve(lines, n)

    print("hello")

if __name__ == "__main__":
    main()  
