first_lim = 10
for col in range(6):
    for row in range(col, first_lim +1, 2):
        print(row, end = "\t" )
    first_lim += 1
    print()
