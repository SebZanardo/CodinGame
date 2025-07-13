import sys
import math

ASH_RUN = 1000
ZOMBIE_RUN = 400

made_it = False
to_protect = 0

while True:
    x, y = [int(i) for i in input().split()]

    human_count = int(input())
    humans = []
    for i in range(human_count):
        # human_id, human_x, human_y
        humans.append(tuple([int(j) for j in input().split()]))

    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        # zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext
        zombies.append(tuple([int(j) for j in input().split()]))

    # Find closest human and run to it only if we can beat zombies
    if not made_it:
        shortest = -1
        z_shortest = -1
        best_h = 0
        for i, h in enumerate(humans):
            distance = math.sqrt((h[1] - x) ** 2 + (h[2] - y) ** 2) / ASH_RUN

            for z in zombies:
                z_dist = math.sqrt((h[1] - z[1]) ** 2 + (h[2] - z[2]) ** 2) / ZOMBIE_RUN

                if z_shortest == -1 or z_dist < z_shortest:
                    z_shortest = z_dist

            if shortest == -1 or (distance < shortest and distance < z_shortest):
                shortest = distance
                best_h = i

        # We have made it to target human
        if shortest == 0 and not made_it:
            made_it = True
            to_protect = humans[best_h][0]

        print(f"{humans[best_h][1]} {humans[best_h][2]}")

    # Chase down zombies closest to human we are protecting
    else:
        g = 0
        for h in humans:
            if h[0] == to_protect:
                g = h
        z_shortest = -1
        best_z = 0
        for i, z in enumerate(zombies):
            z_dist = math.sqrt((g[1] - z[1]) ** 2 + (g[2] - z[2]) ** 2)

            if z_shortest == -1 or z_dist < z_shortest:
                z_shortest = z_dist
                best_z = i

        print(f"{zombies[best_z][1]} {zombies[best_z][2]}")
