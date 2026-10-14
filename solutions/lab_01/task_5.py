researcher_name = input("Введите имя исследователя: ")
experiment_name = input("Введите название эксперимента: ")
runs_count = int(input("Введите количество запусков: "))
run_duration = float(input("Введите длительность одного запуска (в секундах): "))
coeff_real = float(input("Введите действительную часть коэффициента: "))
coeff_imag = float(input("Введите мнимую часть коэффициента: "))

total_seconds = runs_count * run_duration
total_minutes = total_seconds / 60
complex_coeff = complex(coeff_real, coeff_imag)
coeff_modulus_sq = coeff_real**2 + coeff_imag**2
has_runs = bool(runs_count)

print("\n========================================")
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f"Исследователь: {researcher_name}")
print(f"Запуски: {runs_count}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {complex_coeff}")
print(f"Квадрат модуля: {coeff_modulus_sq:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")

print("\n[Диагностика типов введенных данных]")
print(f"1. Имя исследователя:  {type(researcher_name)}")
print(f"2. Название эксперимента:{type(experiment_name)}")
print(f"3. Количество запусков: {type(runs_count)}")
print(f"4. Время одного запуска: {type(run_duration)}")
print(f"5. Движ. часть (re):    {type(coeff_real)}")
print(f"6. Мнимая часть (im):   {type(coeff_imag)}")