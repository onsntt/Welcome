def pendulum(b_ampl, e_ampl):
    count = 0
    while b_ampl > e_ampl:
        b_ampl *= (100 - 8.4) / 100
        count += 1
    return count

begin_amplitude = float(input("Введите начальную амплитуду: "))
end_amplitude = float(input("Введите конечную амплитуду: "))
print("Маятник считается остановившимся через", pendulum(begin_amplitude, end_amplitude), "колебаний.")
