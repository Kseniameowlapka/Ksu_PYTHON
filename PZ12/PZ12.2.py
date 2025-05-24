#Составить генератор (yield), который выводит из строки только буквы.

text = input("Введите строку: ")
for letter in (char for char in text if char.isalpha()):
    print(letter)
