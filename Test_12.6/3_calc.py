def min_dig(num):
    min_d = num % 10
    num //= 10
    while num:
        current_d = num % 10
        if current_d < min_d:
            min_d = current_d
        num //= 10
    print("Минимальная цифра: ", min_d, "\n")

def max_dig(num):
    max_d = num % 10
    num //= 10
    while num:
        current_d = num % 10
        if current_d > max_d:
            max_d = current_d
        num //= 10
    print("Максимальная цифра: ", max_d, "\n" )

def dig_sum(num):
    result = 0
    while num:
        current_d = num % 10
        result += current_d
        num //= 10

    print("Сумма цифр: ", result, "\n")

while True:
    number = int(input("Введите число: "))
    action = int(input("Введите номер действия: \n1 - сумма цифр \n2 - максимальная цифра \n3 - минимальная цифра \n: "))
    if action == 1:
        dig_sum(number)
    elif action == 2:
        max_dig(number)
    elif action == 3:
        min_dig(number)
    else:
        print("Ошибка ввода \n")