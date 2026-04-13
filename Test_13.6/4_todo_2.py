def count_numbers(n):
    count = 0
    while n:
        count += 1
        n //= 10

    return count

def change_digits(num, num_count):
    last_digit = num % 10
    first_digit = num // 10 ** (num_count - 1)
    between_digits = num % 10 ** (num_count - 1) // 10
    return last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit

def main():
    first_n = int(input("Введите первое число: "))
    first_num_count = count_numbers(first_n)
    if first_num_count >= 3:
        first_n = change_digits(first_n, first_num_count)
        print("Изменённое первое число:", first_n)
    else:
        print("В первом числе меньше трёх цифр.")
        exit()
    second_n = int(input("\nВведите второе число: "))
    second_num_count = count_numbers(second_n)
    if second_num_count >= 4:
        second_n = change_digits(second_n, second_num_count)
        print("Изменённое второе число:", second_n)
    else:
        print("Во втором числе меньше четырёх цифр.")
        exit()
    print("\nСумма чисел:", first_n + second_n)
main()