n = int(input("Enter value: "))
if n < 1:
    print("Not good")
counter = 1
while counter <= n:
    print(counter, "** 3 =", counter** 3)
    counter += 1
