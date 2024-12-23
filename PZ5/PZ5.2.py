#Описать функцию RectPS(x1,y1,х2,y2,P,S), вычисляющую периметр P и площадь S
#прямоугольника со сторонами, параллельными осям координат, по координатам (х1,
#y1), (х2, y2) его противоположных вершин (x1, y1, x2, y2 — входные, P и S —
#выходные параметры вещественного типа). С помощью этой функции найти
#периметры и площади трех прямоугольников с данными противоположными
#вершинами.

def RectPS(x1, y1, x2, y2):
    # Вычисляем длину сторон прямоугольника
    width = abs(x2 - x1)  # Ширина
    height = abs(y2 - y1)  # Высота

    # Вычисляем периметр и площадь
    P = 2 * (width + height)  # Периметр
    S = width * height  # Площадь

    return P, S  # Возвращаем периметр и площадь


# Примеры координат противоположных вершин трех прямоугольников
rectangles = [
    (1, 2, 4, 5),  # Прямоугольник 1
    (3, 1, 6, 6),  # Прямоугольник 2
    (-2, -3, 1, 1)  # Прямоугольник 3
]

# Находим периметры и площади для каждого прямоугольника
for i, (x1, y1, x2, y2) in enumerate(rectangles, start=1):
    P, S = RectPS(x1, y1, x2, y2)
    print(f'Прямоугольник {i}: Периметр = {P}, Площадь = {S}')