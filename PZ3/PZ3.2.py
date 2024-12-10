#Спектр видимого излучения представлен в таблице. Составить программу,
#определяющую название цвета в зависимости от введенной длины волны.

def determine_color(wavelength):
    colors = {
        (0, 450): "Фиолетовый",
        (450, 480): "Синий",
        (480, 510): "Сине-зелёный",
        (510, 550): "Зелёный",
        (550, 570): "Жёлто-зелёный",
        (570, 590): "Жёлтый",
        (590, 630): "Оранжевый",
        (630, 700): "Красный"
    }
    
    for (lower, upper), color in colors.items():
        if lower < wavelength <= upper:
            return color
    return "Неизвестный диапазон"


# Ввод пользователя
try:
    wavelength = float(input("Введите длину волны в нм: "))
    color = determine_color(wavelength)
    print(f"Цвет: {color}")
except ValueError:
    print("Введите корректное число.")
