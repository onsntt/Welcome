n = int(input("Enter number "))
for r in range(n + 1):
    for c in range(1, r + 1):
        print(r, end = "\t")
    print()    