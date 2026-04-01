result = 0
number_count = int(input("How many numbers you want to check? "))
for n_c in range(number_count):
    n = int(input("Enter number "))
    divider = False
    for d in range(2, n):
        if n % d == 0:
            divider = True
            break
    if not divider:
            result += 1
print("Количество простых чисел в последовательности:", result)