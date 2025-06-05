#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.
import random

n = 3  
matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i != j:
            matrix[i][j] *= 2

print("\nМатрица после умножения недиагональных элементов на 2:")
for row in matrix:
    print(row)