attempts = 0
guess = 0
number = int(input("Загадайте число от 1 до 10: "))
if not 0 < number < 10:
    print("Неподходящее число")
    exit()
while guess != number:
    guess = int(input("Введите число: "))
    attempts += 1
    if guess > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif guess < number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
print("Вы угадали! Число попыток:", attempts)