def count_letters(txt, x_let, x_num):
    count_letter = 0
    for letter in txt:
        if letter == x_let:
            count_letter += 1
    print("Количество букв", x_let, "в тексте:", count_letter)

    count_number = 0
    for number in txt:
        if number == str(x_num):
            count_number += 1
    print("Количество цифр", x_num, "в тексте:", count_number)

text = input("Введите текст: ")
x_letter = input("Какую букву ищем? ")
x_number =int(input("Какую цифру ищем? "))
count_letters(text, x_letter, x_number)
