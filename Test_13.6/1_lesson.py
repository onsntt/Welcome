def convert_to_float(num):
    mantissa = 0
    exponent = 0
    shifts = 0
    if num < 1:
        while num < 1:
           num *= 10
           exponent -= 1
           mantissa = num
           shifts += 1
        mantissa = round(mantissa, shifts)
        print("Формат плавающей точки: x =", mantissa, "* 10 **", exponent)
    else:
        while num >= 10:
            num /= 10
            exponent += 1
            mantissa = num
            shifts += 1
        mantissa = round(mantissa, shifts)
        print("Формат плавающей точки: x =", mantissa, "* 10 **", exponent)



number = float(input("Введите число: "))
if number > 0:
    convert_to_float(number)
else:
    print("Incorrect value")