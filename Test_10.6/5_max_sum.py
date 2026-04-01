numer_count = int(input("How many numbers you want to check? "))
max_number = 0
max_sum = 0
for n_c in range(numer_count):
    n = int(input("Enter number "))
    storage = n
    num_sum = 0
    while n:
        num_sum += n % 10
        n //= 10
    if num_sum > max_sum:
        max_sum = num_sum
        max_number = storage
print("Число", max_number, "имеет максимальную сумму цифр:", max_sum)