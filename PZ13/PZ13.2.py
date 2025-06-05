# Если в двумерном списке имеются положительные элементы, то вывести TRUE,
#иначе FALSE.

import random

matrix = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]

print("Сгенерированная матрица:")
for row in matrix:
    print(row)

has_positive = any(elem > 0 for row in matrix for elem in row)

print("\nРезультат проверки:", "TRUE" if has_positive else "FALSE")