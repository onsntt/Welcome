heigh = 11
width = 31
for h in range(1, heigh + 1):
    for w in range(1, width + 1):
        if w == 1 or w == width:
            print("|", end = "")
        elif h == 1 or h == heigh:
            print("-", end = "")
        else:
            print(" ", end = "")
    print()
    