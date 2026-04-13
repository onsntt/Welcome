def maximum_of_two(num1, num2):
    if num1 > num2:
        if num1 % 10 == 0:
            num1 = int(num1)
        return num1
    elif num2 > num1:
        if num2 % 10 == 0:
            num2 = int(num2)
        return num2
    else:
        return "Both numbers are equal."

def maximum_of_three(num1,  num2, num3):
    if maximum_of_two(num1, num2) > num3:
        return maximum_of_two(num1, num2)
    elif num3 > maximum_of_two(num1, num2):
        if num3 % 10 == 0:
            num3 = int(num3)
        return num3
    else:
        return "All three numbers are equal."

number1 = float(input("Введите число: "))
number2 = float(input("Введите число: "))
number3 = float(input("Введите число: "))

print("Самое большое число: ", maximum_of_three(number1, number2, number3))