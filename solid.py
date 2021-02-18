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


"""
Open Close Principle
Программные объекты (классы, модули, функции) должны быть открыты для расширения и закрыты для модификации.
"""

# Не правильноый подход.

class Discount:

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
            if self.customer == 'fav':
                return self.price * 0.2
            if self.customer == 'vip':
                return self.price * 0.4


# Правильный подход, один из способов.

from abc import ABC, abstractmethod


class Discount(ABC):

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price


    @abstractmethod
    def give_discount(self):
    	pass


class VIPDiscount(Discount):

	def give_discount(self):
		return self.price * 0.2



class SuperVIPDiscount(VIPDiscount):

    def get_discount(self):
        return self.price * 0.4