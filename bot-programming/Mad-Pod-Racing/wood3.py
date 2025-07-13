# To debug: print("Debug messages...", file=sys.stderr, flush=True)
while True:
    x, y, cx, cy = [int(i) for i in input().split()]
    print(f"{cx} {cy} 100")
