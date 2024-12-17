#Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
#Использовать локальные переменные.

def sum_of_series(n):
    total_sum = 0  
    for i in range(1, n + 1): 
        total_sum += i  
    return total_sum 

# Основная часть программы
n = 60
result = sum_of_series(n)  
print("Сумма чисел от 1 до", n, "равна:", result)
