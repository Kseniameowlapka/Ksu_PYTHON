# Запрос цены 1 кг конфет у пользователя
price_per_kg = float(input("Введите цену 1 кг конфет: "))

# Вывод стоимости от 0.1 до 1 кг
print("Стоимость конфет:")
for kg in range(1, 11):  # от 1 до 10 (0.1 до 1.0)
    weight = kg / 10      # переводим в кг (0.1, 0.2, ..., 1.0)
    cost = weight * price_per_kg
print(f"{weight:.1f} кг: руб.")
