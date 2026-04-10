def summa_n(n):
    result = 0
    for n in range(1, n + 1):
        result += n
    print("Сумма чисел от 1 до", n, "равна", result)

number = int(input("Введите число: "))
summa_n(number)
