#Дан первый член A и знаменатель D геометрической прогрессии. Сформировать и
#вывести список размера 10, содержащий 10 первых членов данной прогрессии: A,
#A* D, A* D^2, A*D^3, ... .

# Вводим первый член A и знаменатель D
A = float(input("Введите первый член A: "))
D = float(input("Введите знаменатель D: "))

# Создаем список для хранения первых 10 членов прогрессии
geometric_progression = []

# Заполняем список первыми 10 членами
for n in range(10):
    term = A * (D ** n)
    geometric_progression.append(term)

# Выводим список
print("Первые 10 членов геометрической прогрессии:")
print(geometric_progression)
