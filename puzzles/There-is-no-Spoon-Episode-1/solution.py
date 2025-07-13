import sys
import math

# Don't let the machines win. You are humanity's last hope...
grid = []
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    row = []
    for char in line:
        if char == '0':
            row.append(True)
        else:
            row.append(False)
    grid.append(row)

for y in range(height):
    for x in range(width):
        if not grid[y][x]:
            continue
        ax = -1
        ay = -1
        bx = -1
        by = -1
        for nx in range(x+1, width):
            if grid[y][nx]:
                ax = nx
                ay = y
                break
        for ny in range(y+1, height):
            if grid[ny][x]:
                by = ny
                bx = x
                break

        print(f"{x} {y} {ax} {ay} {bx} {by}")


