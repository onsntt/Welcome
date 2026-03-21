number  = int(input("Enter value: "))
digit_count = 0
while True:
     number //= 10
     digit_count += 1
     if not number:
          break
print("Your value have", digit_count, "digit(s)." )

