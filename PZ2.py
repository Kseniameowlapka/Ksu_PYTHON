def calculate_distance(V1, V2, S, T): 
    # Суммарная скорость автомобилей 
    total_speed = V1 + V2 
    
    # Общий путь, проделанный автомобилями 
    total_distance_covered = total_speed * T 
    
    # Расстояние между автомобилями через T часов 
    distance_between_cars = S + total_distance_covered 
    
    return distance_between_cars 

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Значение должно быть положительным.")
            return value
        except ValueError as e:
            print(e)

# Пример ввода 
V1 = get_positive_float("Введите скорость первого автомобиля (км/ч): ") 
V2 = get_positive_float("Введите скорость второго автомобиля (км/ч): ") 
S = get_positive_float("Введите расстояние между автомобилями (км): ") 
T = get_positive_float("Введите время (часы): ") 

# Вычисление расстояния между автомобилями через T часов 
result = calculate_distance(V1, V2, S, T) 

print(f"Расстояние между автомобилями через {T} часов составляет {result} км.")