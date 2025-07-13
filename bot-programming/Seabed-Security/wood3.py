# To debug: print("Debug messages...", file=sys.stderr, flush=True)

import sys
from dataclasses import dataclass
import math


@dataclass(slots=True)
class Creature:
    colour: int
    species: int
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0


@dataclass(slots=True)
class Drone:
    x: int = 0
    y: int = 0
    emergency: int = 0
    battery: int = 0


creatures: dict[int, Creature] = {}
drones: dict[int, Drone] = {}
creatures_found = set()

foe_drones: dict[int, Drone] = {}
foe_creatures_found = set()


def main() -> None:
    creature_count = int(input())
    for _ in range(creature_count):
        creature_id, colour, species = [int(j) for j in input().split()]
        creatures[creature_id] = Creature(colour, species)

    while True:
        # INPUT ###############################################################
        my_score = int(input())
        foe_score = int(input())

        my_scan_count = int(input())
        for _ in range(my_scan_count):
            creature_id = int(input())
            creatures_found.add(creature_id)

        foe_scan_count = int(input())
        for _ in range(foe_scan_count):
            creature_id = int(input())
            foe_creatures_found.add(creature_id)

        my_drone_count = int(input())
        for _ in range(my_drone_count):
            drone_id, x, y, emergency, battery = [int(j) for j in input().split()]
            drones[drone_id] = Drone(x, y, emergency, battery)

        foe_drone_count = int(input())
        for _ in range(foe_drone_count):
            drone_id, x, y, emergency, battery = [int(j) for j in input().split()]
            foe_drones[drone_id] = Drone(x, y, emergency, battery)

        # NOTE: No clue what this is
        drone_scan_count = int(input())
        for _ in range(drone_scan_count):
            drone_id, creature_id = [int(j) for j in input().split()]

        visible_creature_count = int(input())
        for _ in range(visible_creature_count):
            creature_id, x, y, vx, vy = [int(j) for j in input().split()]
            creatures[creature_id].x = x
            creatures[creature_id].y = y
            creatures[creature_id].vx = vx
            creatures[creature_id].vy = vy

        # NOTE: No clue what this is
        radar_blip_count = int(input())
        for _ in range(radar_blip_count):
            inputs = input().split()
            drone_id = int(inputs[0])
            creature_id = int(inputs[1])
            radar = inputs[2]

        # LOGIC ###############################################################
        for drone_id, drone in drones.items():
            tx = -1
            ty = -1
            light = 0

            min_dist = -1
            target_creature = None

            for creature_id, creature in creatures.items():
                # Skip any fish already found
                if creature_id in creatures_found:
                    continue

                # Calculate distance to unfound fish --> track closest
                x_diff = (drone.x - creature.x)
                y_diff = (drone.y - creature.y)
                dist = math.sqrt(x_diff ** 2 + y_diff ** 2)

                if target_creature is None or dist < min_dist:
                    min_dist = dist
                    target_creature = creature
                    tx = creature.x
                    ty = creature.y

            # OUTPUT ##########################################################
            # MOVE <x> <y> <light (1|0)> | WAIT <light (1|0)>
            if my_scan_count == creature_count or (tx == -1 and ty == -1):
                print(f"WAIT {light}")
            else:
                print(f"MOVE {tx} {ty} {light}")


main()
