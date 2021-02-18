# SOLID

"""
Single Responsibility Principle
Приниц единой ответственности - каждый объект должен иметь одну обязанность и эта обязанность должна быть
полностью инкапсулирована в класс. Все его сервисы должны быть направлены исключительно на обеспечение этой обязанности.

"""

# Не правильный подход. У класса несколько обязанностей.
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass



# Правильный пример. Разделили обязанности класса.
class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass