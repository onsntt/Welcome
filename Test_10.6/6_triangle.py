height = int(input("Enter height "))
width = 1+2*(height - 1)
for h in range(1, height + 1):
    for w in range(1, width+ 1):
        if w <= (width // 2 + 1) - h  or w >= (width // 2 + 1 ) + h:
            print(" ", end = "")
        else:
            print("#", end = "")
    print()