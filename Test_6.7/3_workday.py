task_counter = 0
tel_answer = 0
workhours = 0
print("Начался восьмичасовой рабочий день.")
while workhours < 8:
    workhours += 1
    print(workhours,'- й час')
    task_per_hour = int(input("Сколько задач решит Максим? "))
    task_counter += task_per_hour
    if not tel_answer:
        slavery = int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
        if slavery:
            tel_answer += 1
print("Рабочий день закончился.")
print("Всего выполнено задач:", task_counter)
if tel_answer:
    print("Нужно зайти в магазин.")


