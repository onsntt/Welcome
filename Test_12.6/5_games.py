import random
def rock_paper_scissors():
  # Здесь будет игра «Камень, ножницы, бумага»
    variant = input("Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага: ")
    if variant == "1":
        print("Вы выбрали Камень.")
        comp_choice = random.choice(["Ножницы", "Бумага"])
        if comp_choice == "Ножницы":
            print("Компьютер выбрал Ножницы. Вы выиграли!")
        else:
            print("Компьютер выбрал Бумага. Вы проиграли!")

    elif variant == "2":
        print("Вы выбрали Ножницы.")
        comp_choice = random.choice(["Камень", "Бумага"])
        if comp_choice == "Камень":
            print("Компьютер выбрал Камень. Вы проиграли!")
        else:
            print("Компьютер выбрал Бумага. Вы выиграли!")
    elif variant == '3':
        print("Вы выбрали Бумага.")
        comp_choice = random.choice(["Камень", "Ножницы"])
        if comp_choice == "Камень":
            print("Компьютер выбрал Камень. Вы выиграли!")
        else:
            print("Компьютер выбрал Ножницы. Вы проиграли!")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        rock_paper_scissors()

    main_menu()

def guess_the_number():
  # Здесь будет игра «Угадай число»
    number_to_guess = random.randint(1, 10)

    while True:
        guess = int(input("Угадайте число от 1 до 10: "))

        if guess < number_to_guess:
            print("Слишком мало! Попробуйте снова.")
        elif guess > number_to_guess:
            print("Слишком много! Попробуйте снова.")
        else:
            print("Поздравляем! Вы угадали число",number_to_guess, "!")
            break
    main_menu()

def main_menu():
  # Здесь главное меню игры
    choice = input("Выберите игру: 1 - Камень, ножницы, бумага; 2 - Угадай число: ")
    if choice == "1":
        rock_paper_scissors()
    elif choice == "2":
        guess_the_number()
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")
        main_menu()

main_menu()