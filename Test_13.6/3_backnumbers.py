def revert_number(num):
    result = ""
    while num > 0:
        result += str(num % 10)
        num //= 10
    return int(result)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print("Первое число наоборот:", revert_number(number1))
print("Второе число наоборот:", revert_number(number2))