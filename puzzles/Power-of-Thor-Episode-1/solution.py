light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

x = initial_tx
y = initial_ty
while True:
    remaining_turns = int(input())

    direction = ''
    if light_y > y:
        direction += 'S'
        y += 1
    elif light_y < y:
        direction += 'N'
        y -= 1

    if light_x > x:
        direction += 'E'
        x += 1
    elif light_x < x:
        direction += 'W'
        x -= 1

    print(direction)

