import sys
import math


w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]

lx = 0
rx = w
x = x0

ly = 0
ry = h
y = y0

while True:
    d = input()

    if 'U' in d:
        ry = y
        y = int((ly + ry) / 2)
    elif 'D' in d:
        ly = y
        y = int((ly + ry) / 2)

    if 'L' in d:
        rx = x
        x = int((lx + rx) / 2)
    elif 'R' in d:
        lx = x
        x = int((lx + rx) / 2)


    print(f"{x} {y}")

