# Если в двумерном списке имеются положительные элементы, то вывести TRUE,
#иначе FALSE.

matrix = [
    [-1, -2, 0],
    [-4, -5, -6],
    [-7, -8, -9]
]

# Проверка наличия положительных элементов
has_positive = any(elem > 0 for row in matrix for elem in row)

# Вывод результата
print("TRUE" if has_positive else "FALSE")
