#В двумерном списке все элементы, не лежащие на главной диагонали увеличить в 2
#раза.
import random

import random

M = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]

print("Сгенерированная матрица:")
for row in M:
    print(row)

M = list(map(lambda i_row: list(map(lambda j_x: j_x[1]*2 if i_row[0]!=j_x[0] else j_x[1], enumerate(i_row[1]))), enumerate(M)))

print("\nИзменённая:")
for row in M:
    print(row)