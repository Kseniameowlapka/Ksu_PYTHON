#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.
import random

def modify_matrix(m):
    return [[x*2 if i!=j else x for j,x in enumerate(row)] for i,row in enumerate(m)]

n = 3
matrix = [[random.randint(1,10) for _ in range(n)] for _ in range(n)]

print("Исходная:")
[print(row) for row in matrix]

print("\nИзменённая:")
[print(row) for row in modify_matrix(matrix)]