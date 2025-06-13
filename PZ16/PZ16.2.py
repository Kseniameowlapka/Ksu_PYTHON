# Создайте класс "Животное", который содержит информацию о виде и возрасте
#животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
#"Животное" и содержат информацию о породе
class Animal:
    def __init__(self, species, age):
        self.species = species  # Вид животного
        self.age = age          # Возраст животного

    def get_info(self):
        return f"Вид: {self.species}, Возраст: {self.age} лет"

class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)  # Наследуем свойства от Animal
        self.breed = breed             # Порода собаки

    def get_info(self):
        base_info = super().get_info()  # Получаем базовую информацию
        return f"{base_info}, Порода: {self.breed}"

class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)  # Наследуем свойства от Animal
        self.breed = breed             # Порода кошки

    def get_info(self):
        base_info = super().get_info()  # Получаем базовую информацию
        return f"{base_info}, Порода: {self.breed}"

# Пример использования
dog = Dog("Собака", 5, "Лабрадор")
cat = Cat("Кошка", 3, "Британская")

print(dog.get_info()) 
print(cat.get_info())  