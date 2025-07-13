x, y, a, b = [int(i) for i in input().split()]
while True:
    remaining_turns = int(input())
    s = ''
    if b > y:
        s += 'N'
        b -= 1
    if b < y:
        s += 'S'
        b += 1
    if a > x:
        s += 'W'
        a -= 1
    if a < x:
        s += 'E'
        a += 1
    print(s)
