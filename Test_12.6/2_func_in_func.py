def positive(value):
    print("Число", value, "является положительным")
    test()

def negative(value):
    print("Число", value, "является отрицательным")
    test()

def test():
    number = int(input("Введите число: "))
    if number > 0:
        positive(number)
    elif number < 0:
        negative(number)
    else:
        print("Мы насчет нуля не договаривались!")
        
test()
