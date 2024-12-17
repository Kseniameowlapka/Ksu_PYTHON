#Спектр видимого излучения представлен в таблице. Составить программу,
#определяющую название цвета в зависимости от введенной длины волны.

def determine_color(wavelength):
    if wavelength <= 450:
        return "Фиолетовый"
    elif 450 < wavelength <= 480:
        return "Синий"
    elif 480 < wavelength <= 510:
        return "Сине-зелёный"
    elif 510 < wavelength <= 550:
        return "Зелёный"
    elif 550 < wavelength <= 570:
        return "Жёлто-зелёный"
    elif 570 < wavelength <= 590:
        return "Жёлтый"
    elif 590 < wavelength <= 630:
        return "Оранжевый"
    elif wavelength >= 630:
        return "Красный"
    else:
        return "Неизвестный диапазон"


# Ввод пользователя
try:
    wavelength = float(input("Введите длину волны в нм: "))
    color = determine_color(wavelength)
    print(f"Цвет: {color}")
except ValueError:
    print("Введите корректное число.")
