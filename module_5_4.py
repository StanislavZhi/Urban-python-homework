
class House:
    # Атрибут класса для хранения истории всех созданных домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        """Создание объекта и запись его в историю."""
        if args:
            name = args[0]  # Название дома (первый аргумент)
            cls.houses_history.append(name)  # Добавляем в историю
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        """Инициализация объекта."""
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        """Строковое представление объекта."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        """Сообщение при удалении объекта."""
        print(f"{self.name} снесён, но он останется в истории")

# === Пример использования ===

# Создание объектов
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
