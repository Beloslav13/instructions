"""
Интерфейсы.
Если это выглядит как утка, плавает как утка и крякает как утка, то это, вероятно, и есть утка.

Структура интерфейса:
- класс интерфейса (абстрактный класс (наследующий abc.ABC))
- поля интерфейса (абстрактные свойства (@property + @abstractmethod))
- методы интерфейса (абсктрактные методы (@abstractmethod))
- typing (подсказки типов)

В чем отличие от простого абстрактного классса? Абстрактный класс реализует дополнительные методы.
"""

from abc import ABC, abstractmethod


class Interface(ABC):

	@property
	@abstractmethod
	def prop(self):
		pass	

	@abstractmethod
	def method(self):
		pass


class InterfaceImpl(Interface):

	@property
	def prop(self):
		return 'Свойство переопределено'

	def method(self):
		print(self.prop)


# Еще пример
class Dob(ABC):
	"""
	Интрефейс `собака`
	Поле интерфейса "имя собаки" задано как абстрактное свойство, а не через конструктор __init__(self,name)
	"""

	@property
	@abstractmethod
	def name(self) -> str:
		pass

	@abstractmethod
	def bark(self) -> None:
		pass


class BullDog(Dob):

	def __init__(self, name: str):
		self._name = name

	@property
	def name(self):
		return self._name

	def bark(self):
		print(f'{self.__class__.__name__} {self.name} говорит гав.')
