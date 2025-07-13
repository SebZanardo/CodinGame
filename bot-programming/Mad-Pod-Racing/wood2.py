# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def clamp(x: float, lo: float, hi: float) -> float:
    return max(min(x, hi), lo)


MAX_THRUST = 100
MIN_THRUST = 0


while True:
    x, y, cx, cy, cd, ca = [int(i) for i in input().split()]
    ox, oy = [int(i) for i in input().split()]
    thrust = (1 - abs(ca) / 180) * MAX_THRUST
    thrust = int(clamp(thrust, MIN_THRUST, MAX_THRUST))
    print(f"{cx} {cy} {thrust}")
