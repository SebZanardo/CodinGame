# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def clamp(x: float, lo: float, hi: float) -> float:
    return max(min(x, hi), lo)


MAX_THRUST = 100
MIN_THRUST = 0
MIN_TURN_THRUST = 20
BOOST_DIST = 6000
BOOST_ANG = 3
SLOW_DIST = 2000
SLOW_MULT = 20


boosted = False


while True:
    x, y, cx, cy, cd, ca = [int(i) for i in input().split()]
    ox, oy = [int(i) for i in input().split()]
    thrust = (1 - abs(ca) / 180) * MAX_THRUST + MIN_TURN_THRUST
    thrust = int(clamp(thrust, MIN_THRUST, MAX_THRUST))
    if cd < SLOW_DIST and cd > 0:
        thrust -= SLOW_DIST / cd * SLOW_MULT
    thrust = int(clamp(thrust, MIN_THRUST, MAX_THRUST))
    if cd > BOOST_DIST and abs(ca) < BOOST_ANG and not boosted:
        thrust = "BOOST"
        boosed = True
    print(f"{cx} {cy} {thrust}")
