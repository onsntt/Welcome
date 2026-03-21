deposit = int(input("Вклад в банке: "))
percent = int(input("Проценты: "))
final_summ = int(input("Порог вклада: "))
years = 0
while True:
    years += 1
    deposit += int((deposit * percent / 100))
    print(years, "год.", deposit, "+", percent, "% =", deposit)
    if deposit >= final_summ:
        print("Кол-во лет для достижения порога: ", years)
        break